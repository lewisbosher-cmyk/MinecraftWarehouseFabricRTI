# Minecraft Education Code Builder (Python)
# Worker-only script. Assumes warehouse has already been built at fixed coordinates.

ORIGIN_X = 100
ORIGIN_Y = 4
ORIGIN_Z = 100

fabric_eventhouse_name = "<SET_EVENT_HUB_NAME>"
fabric_event_stream_endpoint = "<SET_CONNECTION_STRING_IN_FABRIC_BRIDGE>"
fabric_access_key = "<SET_SAS_KEY_IN_FABRIC_BRIDGE>"
# Seed with a string so MakeCode infers string[] (not any[]), then clear it.
event_buffer = [""]
event_buffer.pop()
fabric_bridge_outbox = [""]
fabric_bridge_outbox.pop()
event_sequence = 0
fabric_sent_count = 0
shift_running = False

sections = [
    {"name": "Loading_Bay", "minX": 102, "maxX": 118, "minY": 4, "maxY": 12, "minZ": 102, "maxZ": 116},
    {"name": "Storage_Area_A", "minX": 122, "maxX": 158, "minY": 4, "maxY": 12, "minZ": 102, "maxZ": 128},
    {"name": "Storage_Area_B", "minX": 122, "maxX": 158, "minY": 4, "maxY": 12, "minZ": 130, "maxZ": 144},
    {"name": "Packing_Station", "minX": 102, "maxX": 118, "minY": 4, "maxY": 12, "minZ": 118, "maxZ": 128},
    {"name": "Forbidden_Zone", "minX": 102, "maxX": 118, "minY": 4, "maxY": 12, "minZ": 130, "maxZ": 144},
    {"name": "Control_Office", "minX": 160, "maxX": 170, "minY": 4, "maxY": 12, "minZ": 102, "maxZ": 114}
]

# Absolute-coordinate bounds for the two storage sections.
STORAGE_BOUNDS = [
    {"minX": 125, "maxX": 160, "minY": 5, "maxY": 13, "minZ": 132, "maxZ": 142},
    {"minX": 125, "maxX": 155, "minY": 5, "maxY": 11, "minZ": 104, "maxZ": 126}
]

PLACEABLE_BLOCKS = [
    {"name": "CHEST",          "type": CHEST},
    {"name": "BARREL",         "type": BARREL},
    {"name": "HAY_BLOCK",      "type": HAY_BLOCK},
    {"name": "BOOKSHELF",      "type": BOOKSHELF},
    {"name": "GOLD_BLOCK",     "type": GOLD_BLOCK},
    {"name": "IRON_BLOCK",     "type": IRON_BLOCK},
    {"name": "DIAMOND_BLOCK",  "type": DIAMOND_BLOCK},
    {"name": "EMERALD_BLOCK",  "type": EMERALD_BLOCK},
    {"name": "COAL_BLOCK",     "type": COAL_BLOCK},
    {"name": "REDSTONE_BLOCK", "type": REDSTONE_BLOCK}
]


def point(dx, dy, dz):
    return {
        "p": world(ORIGIN_X + dx, ORIGIN_Y + dy, ORIGIN_Z + dz),
        "x": ORIGIN_X + dx,
        "y": ORIGIN_Y + dy,
        "z": ORIGIN_Z + dz
    }


def abs_point(x, y, z):
    return {"p": world(x, y, z), "x": x, "y": y, "z": z}


def random_storage_point(section_index):
    s = STORAGE_BOUNDS[section_index]
    x = Math.randomRange(s["minX"], s["maxX"])
    y = Math.randomRange(s["minY"], s["maxY"])
    z = Math.randomRange(s["minZ"], s["maxZ"])
    return abs_point(x, y, z)


def random_block():
    return PLACEABLE_BLOCKS[Math.randomRange(0, len(PLACEABLE_BLOCKS) - 1)]


def section_for_position(x, y, z):

    i = 0
    while i < len(sections):
        s = sections[i]
        if x >= s["minX"] and x <= s["maxX"] and y >= s["minY"] and y <= s["maxY"] and z >= s["minZ"] and z <= s["maxZ"]:
            return s["name"]
        i += 1

    return "Outside_Warehouse"


def event_to_json(event_type, block_name, x, y, z, ts):
    location = section_for_position(x, y, z)

    payload = '{"event_type":"' + event_type + '",' + \
        '"block":"' + block_name + '",' + \
        '"x":' + str(x) + ',' + \
        '"y":' + str(y) + ',' + \
        '"z":' + str(z) + ',' + \
        '"location":"' + location + '",' + \
        '"minecraft_time":' + str(ts) + \
        '}'
    return payload


def send_to_fabric_event_stream(payload):
    global fabric_sent_count
    if len(fabric_event_stream_endpoint) > 0 and len(fabric_access_key) > 0:
        # Minecraft Code Builder Python does not support direct outbound HTTP.
        # Emit bridge-ready records for forwarding to Fabric outside the game.
        fabric_bridge_outbox.append(payload)
        fabric_sent_count += 1
        player.say("FABRIC_EVENT|" + payload)


def emit_event(event_type, block_name, pt):
    global event_sequence
    event_sequence += 1
    payload = event_to_json(event_type, block_name, pt["x"], pt["y"], pt["z"], event_sequence)
    event_buffer.append(payload)
    send_to_fabric_event_stream(payload)


def travel_agent_to(pt):
    agent.teleport(pt["p"], NORTH)
    # Small visible movement so the worker appears active, not just teleporting.
    agent.move(FORWARD, 1)
    loops.pause(150)
    agent.move(BACK, 1)
    emit_event("Agent_Travelled", "AGENT", pt)


def move_block(block_name, source, destination, block_type):
    # Only remove if there is actually a block at the source (not AIR).
    if blocks.test_for_block(AIR, source["p"]) == False:
        travel_agent_to(source)
        blocks.place(AIR, source["p"])
        emit_event("Block_Removed", block_name, source)
    else:
        player.say("SKIP remove " + block_name + ": no block at source")

    # Only place if the destination slot is empty (AIR).
    if blocks.test_for_block(AIR, destination["p"]) == True:
        travel_agent_to(destination)
        blocks.place(block_type, destination["p"])
        emit_event("Block_Placed", block_name, destination)
    else:
        player.say("SKIP place " + block_name + ": destination already occupied")


def run_warehouse_shift():
    # One cycle of warehouse work. Called repeatedly by loops.forever when enabled.
    block = random_block()
    # Pick a random destination section (0 = Storage 1, 1 = Storage 2).
    section_idx = Math.randomRange(0, 1)
    src = point(6, 1, 10)
    dst = random_storage_point(section_idx)
    move_block(block["name"], src, dst, block["type"])

    player.say(
        "Shift cycle complete. Events: " + str(len(event_buffer)) +
        " Fabric bridge queued: " + str(fabric_sent_count)
    )


def log_section_coordinates():
    player.say("Warehouse section coordinates:")
    i = 0
    while i < len(sections):
        s = sections[i]
        player.say(
            s["name"] +
            " X:" + str(s["minX"]) + "-" + str(s["maxX"]) +
            " Y:" + str(s["minY"]) + "-" + str(s["maxY"]) +
            " Z:" + str(s["minZ"]) + "-" + str(s["maxZ"])
        )
        i += 1


def on_run_shift():
    global shift_running
    shift_running = True
    player.say("Infinite shift started. Use: stop_shift")


def on_stop_shift():
    global shift_running
    shift_running = False
    player.say("Shift stopped.")


def on_show_fabric_queue():
    player.say("Fabric bridge queue count: " + str(len(fabric_bridge_outbox)))
    i = 0
    while i < len(fabric_bridge_outbox):
        player.say("FABRIC_EVENT|" + fabric_bridge_outbox[i])
        i += 1


def on_show_events():
    player.say("Event buffer count: " + str(len(event_buffer)))
    i = 0
    while i < len(event_buffer):
        player.say(event_buffer[i])
        i += 1


def on_show_coords():
    log_section_coordinates()


def on_set_fabric_placeholder():
    global fabric_eventhouse_name
    global fabric_event_stream_endpoint
    global fabric_access_key
    fabric_eventhouse_name = "esehusw3ubkjed82txblsk7m_eh"
    fabric_event_stream_endpoint = "<PASTE_FABRIC_EVENTSTREAM_ENDPOINT>"
    fabric_access_key = "yURwkG1jXx2NbDv0iGvPJkeZtTHQwjeqF+AEhI9EmsM="
    player.say("Fabric credentials and Eventhouse name applied.")


def shift_worker_loop():
    if shift_running:
        run_warehouse_shift()
        loops.pause(2000)
    else:
        loops.pause(200)


player.on_chat("run_shift", on_run_shift)
player.on_chat("stop_shift", on_stop_shift)
player.on_chat("show_events", on_show_events)
player.on_chat("show_fabric_queue", on_show_fabric_queue)
player.on_chat("show_coords", on_show_coords)
player.on_chat("set_fabric_placeholder", on_set_fabric_placeholder)
loops.forever(shift_worker_loop)
