# Fabric Eventstream Bridge — Minecraft WebSocket Server
#
# Flow:
#   1. Run this script:              python fabric_bridge.py
#   2. In Minecraft Education chat:  /connect localhost:3000
#   3. Run warehouse_worker.py in Code Builder and type: run_shift
#   4. Events stream: Minecraft -> WebSocket -> Fabric Eventstream -> KQL Table
#
# Subscribes to: PlayerMessage (FABRIC_EVENT| chat lines from warehouse_worker.py),
#                BlockPlaced, BlockBroken, PlayerTravelled
#
# Requires: pip install websockets azure-eventhub

import asyncio
import json
import os
import uuid
import websockets
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

FABRIC_EVENT_STREAM_CONNECTION_STRING = os.getenv("FABRIC_EVENT_STREAM_CONNECTION_STRING", "")
EVENT_HUB_NAME = os.getenv("EVENT_HUB_NAME", "")
HOST = os.getenv("BRIDGE_HOST", "localhost")
PORT = int(os.getenv("BRIDGE_PORT", "3000"))
PREFIX = "FABRIC_EVENT|"

SECTIONS = [
    {"name": "Loading_Bay",     "minX": 102, "maxX": 118, "minY": 4, "maxY": 12, "minZ": 102, "maxZ": 116},
    {"name": "Storage_Area_A",  "minX": 122, "maxX": 158, "minY": 4, "maxY": 12, "minZ": 102, "maxZ": 128},
    {"name": "Storage_Area_B",  "minX": 122, "maxX": 158, "minY": 4, "maxY": 12, "minZ": 130, "maxZ": 144},
    {"name": "Packing_Station", "minX": 102, "maxX": 118, "minY": 4, "maxY": 12, "minZ": 118, "maxZ": 128},
    {"name": "Forbidden_Zone",  "minX": 102, "maxX": 118, "minY": 4, "maxY": 12, "minZ": 130, "maxZ": 144},
    {"name": "Control_Office",  "minX": 160, "maxX": 170, "minY": 4, "maxY": 12, "minZ": 102, "maxZ": 114},
]


def section_for_position(x, y, z):
    for s in SECTIONS:
        if s["minX"] <= x <= s["maxX"] and s["minY"] <= y <= s["maxY"] and s["minZ"] <= z <= s["maxZ"]:
            return s["name"]
    return "Outside_Warehouse"


def subscribe_msg(event_name):
    return json.dumps({
        "header": {
            "version": 1,
            "requestId": str(uuid.uuid4()),
            "messagePurpose": "subscribe",
            "messageType": "commandRequest",
        },
        "body": {"eventName": event_name},
    })


def validate_config():
    missing = []
    if not FABRIC_EVENT_STREAM_CONNECTION_STRING:
        missing.append("FABRIC_EVENT_STREAM_CONNECTION_STRING")
    if not EVENT_HUB_NAME:
        missing.append("EVENT_HUB_NAME")

    if missing:
        raise RuntimeError(
            "Missing required environment variables: " + ", ".join(missing) +
            ". Set them before running fabric_bridge.py"
        )


async def send_to_fabric(producer, payload_str):
    try:
        batch = await producer.create_batch()
        batch.add(EventData(payload_str))
        await producer.send_batch(batch)
        print(f"[fabric] -> {payload_str}", flush=True)
    except Exception as e:
        print(f"[fabric] SEND FAILED: {type(e).__name__}: {e}", flush=True)


async def handle_minecraft(websocket, producer):
    print(f"[bridge] Minecraft connected!", flush=True)

    for event in ["PlayerMessage", "BlockPlaced", "BlockBroken", "PlayerTravelled"]:
        await websocket.send(subscribe_msg(event))
    print("[bridge] Subscribed to events. Run warehouse_worker.py in Code Builder, then type: run_shift", flush=True)

    try:
        async for raw in websocket:
            try:
                msg = json.loads(raw)
                header = msg.get("header", {})
                body = msg.get("body", {})

                purpose = header.get("messagePurpose", "")
                event_name = header.get("eventName", "")
                print(f"[debug] RAW purpose={purpose!r} event={event_name!r} body_keys={list(body.keys())}", flush=True)
                if purpose == "error":
                    print(f"[debug] ERROR body: statusCode={body.get('statusCode')} statusMessage={body.get('statusMessage')!r}", flush=True)

                if purpose == "event" and event_name == "PlayerMessage":
                    print(f"[debug] PlayerMessage body={body}", flush=True)

                if header.get("messagePurpose") != "event":
                    continue

                print(f"[debug] Event received: {event_name}", flush=True)

                if event_name == "PlayerMessage":
                    message = body.get("message", "")
                    print(f"[debug] PlayerMessage received: {repr(message)}", flush=True)
                    if PREFIX in message:
                        payload_str = message[message.index(PREFIX) + len(PREFIX):]
                        try:
                            json.loads(payload_str)
                            await send_to_fabric(producer, payload_str)
                        except json.JSONDecodeError:
                            print(f"[bridge] Invalid JSON in chat: {payload_str}", flush=True)
                    else:
                        print(f"[debug] No FABRIC_EVENT| prefix found in message", flush=True)

                elif event_name in ("BlockPlaced", "BlockBroken"):
                    pos = body.get("position", {})
                    x = int(pos.get("x", 0))
                    y = int(pos.get("y", 0))
                    z = int(pos.get("z", 0))
                    payload = json.dumps({
                        "event_type": "Block_Placed" if event_name == "BlockPlaced" else "Block_Broken",
                        "block": body.get("blockName", "unknown"),
                        "x": x, "y": y, "z": z,
                        "location": section_for_position(x, y, z),
                        "player": body.get("player", {}).get("name", "unknown"),
                        "minecraft_time": body.get("worldTime", 0),
                    })
                    await send_to_fabric(producer, payload)

                elif event_name == "PlayerTravelled":
                    pos = body.get("player", {}).get("position", {})
                    x = round(float(pos.get("x", 0)))
                    y = round(float(pos.get("y", 0)))
                    z = round(float(pos.get("z", 0)))
                    payload = json.dumps({
                        "event_type": "Player_Travelled",
                        "block": "PLAYER",
                        "x": x, "y": y, "z": z,
                        "location": section_for_position(x, y, z),
                        "player": body.get("player", {}).get("name", "unknown"),
                        "minecraft_time": body.get("worldTime", 0),
                    })
                    await send_to_fabric(producer, payload)

            except Exception as e:
                print(f"[bridge] Error: {e}", flush=True)
    except (websockets.exceptions.ConnectionClosedError, websockets.exceptions.ProtocolError) as e:
        # Minecraft Education sends non-standard WebSocket close frames; log and continue.
        print(f"[bridge] Minecraft disconnected: {e}", flush=True)


async def main():
    validate_config()
    async with EventHubProducerClient.from_connection_string(
        conn_str=FABRIC_EVENT_STREAM_CONNECTION_STRING,
        eventhub_name=EVENT_HUB_NAME,
    ) as producer:
        print(f"[bridge] Connected to Fabric Eventstream.", flush=True)
        print(f"[bridge] WebSocket server listening on ws://{HOST}:{PORT}", flush=True)
        print(f"[bridge] In Minecraft Education chat type:  /connect {HOST}:{PORT}", flush=True)

        async with websockets.serve(
            lambda ws: handle_minecraft(ws, producer),
            HOST, PORT,
            ping_interval=None,
            ping_timeout=None,
            subprotocols=["com.microsoft.minecraft.ws"],
        ):
            await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
