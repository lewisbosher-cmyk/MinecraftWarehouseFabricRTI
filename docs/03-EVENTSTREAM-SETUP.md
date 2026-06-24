# 3️⃣ EventStream Configuration

Connect your Minecraft events to Fabric Eventstream using the Eventstream-managed Event Hub endpoint.

## 🌊 Architecture Overview

```
┌─────────────────────────────┐
│  Minecraft Education        │
│  (Event Generation)         │
└──────────┬──────────────────┘
           │ /connect localhost:3000
           ↓
┌─────────────────────────────┐
│  WebSocket Server           │
│  (Python: fabric_bridge.py) │
│  listens on localhost:3000  │
└──────────┬──────────────────┘
           │ Events via SDK
           ↓
┌─────────────────────────────┐
│  Fabric Eventstream Source  │
│  Custom Endpoint            │
│  Protocol: Event Hub        │
│  Auth: SAS Key              │
└──────────┬──────────────────┘
           │
           ↓
┌─────────────────────────────┐
│  Fabric Eventstream         │
│  (Real-time data hub)       │
└──────────┬──────────────────┘
           │
           ↓
┌─────────────────────────────┐
│  Eventhouse (KQL Tables)    │
│  (Data warehouse)           │
└─────────────────────────────┘
```

---

## 🔧 Setup Steps

### Step 1: Create Eventstream and Source

1. **Go to your Fabric workspace**
   - Open [fabric.microsoft.com](https://fabric.microsoft.com)
   - Open your `Minecraft-RTI` workspace

2. **Create Eventstream**
   - Click `+ New`
   - Select `Eventstream`
   - Name it `minecraft-warehouse-events`

3. **Add source as Custom Endpoint**
   - In the Eventstream canvas, click `+ Add source`
   - Choose `Custom endpoint`
   - Click the new source node to open settings

4. **Set source protocol and auth**
   - **Protocol**: `Event Hub`
   - **Authentication**: `SAS Key`

### Step 2: Copy Event Hub Credentials from Eventstream Source

From the source configuration pane, copy the required values shown there:

- Namespace/Endpoint (sb://...)
- Event Hub name (entity path)
- SAS Key Name
- SAS Key

Build the connection string in this format:

```text
Endpoint=sb://<namespace>.servicebus.windows.net/;SharedAccessKeyName=<sas-key-name>;SharedAccessKey=<sas-key>;EntityPath=<event-hub-name>
```

This is the connection string your Python bridge will use.

### Step 3: Update fabric_bridge.py

1. Open `fabric_bridge.py`
2. Replace connection values with the ones copied from Eventstream source settings

```python
FABRIC_EVENT_STREAM_CONNECTION_STRING = "Endpoint=sb://<namespace>.servicebus.windows.net/;SharedAccessKeyName=<sas-key-name>;SharedAccessKey=<sas-key>;EntityPath=<event-hub-name>"
EVENT_HUB_NAME = "<event-hub-name>"
```

3. Save the file.

### Step 4: Start WebSocket Server

1. Open terminal and go to project folder
2. Activate virtual environment:

```bash
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

3. Start bridge:

```bash
python fabric_bridge.py
```

4. Expected output:

```text
WebSocket server listening on ws://localhost:3000
Waiting for Minecraft connections...
```

### Step 5: Connect Minecraft to Local Bridge

1. In Minecraft chat:

```text
/connect localhost:3000
```

2. In bridge terminal, verify connection message appears.

---

## 🚀 Running Your First Events

### Generate Test Event

In Minecraft chat:

```text
FABRIC_EVENT|{"event_type":"test","agent_name":"worker","location":"Loading_Bay","timestamp":"2024-01-15T10:00:00Z","items":5}
```

Expected in bridge terminal:

```text
Event received: FABRIC_EVENT|{"event_type":"test",...}
Sending to Event Hub: <event-hub-name>
```

### Start Warehouse Worker

In Minecraft chat:

```text
run_shift
```

Expected:

- Agent runs warehouse steps
- Events emit every operation
- Bridge logs event forwarding

---

## 📊 Eventstream Verification

1. Open Eventstream in Fabric
2. Select your source
3. Open `Preview`/`Live data`
4. Confirm events arrive with current timestamps

### Add Destination to Eventhouse (Recommended)

1. In the same Eventstream canvas, click `+ Add destination`
2. Choose `Eventhouse`
3. Select your workspace and Eventhouse item
4. Fill destination details (database/table names)
5. Save destination

After destination configuration is complete, Eventstream will create/populate a raw KQL table automatically. You do not need to manually map individual columns for the initial raw table.

Optional source transform:

```kql
| extend timestamp = todatetime(timestamp)
| extend items_processed = tolong(items_processed)
| extend efficiency_score = todouble(efficiency_score)
```

Optional source transform:

```kql
| extend timestamp = todatetime(timestamp)
| extend items_processed = tolong(items_processed)
| extend efficiency_score = todouble(efficiency_score)
```

---

## 🎯 Testing Connectivity

### Test 1: WebSocket Listener

```bash
netstat -ano | findstr :3000  # Windows
lsof -i :3000                 # macOS/Linux
```

### Test 2: Minecraft Message Flow

```text
FABRIC_EVENT|{"test":"message"}
```

Bridge terminal should log receipt and forward attempt.

### Test 3: Eventstream Source Preview

Confirm the source preview shows the test events.

---

## 🐛 Troubleshooting

### "Connection refused"

Symptom:

```text
/connect localhost:3000 fails
```

Fix:

1. Start bridge: `python fabric_bridge.py`
2. Verify port 3000 not blocked
3. If needed, free port and retry

### "No events appearing in Eventstream"

Symptom:

```text
Minecraft connected, but source preview is empty
```

Fix:

1. Validate `FABRIC_EVENT|` prefix exists
2. Validate payload JSON format
3. Re-copy credentials from Eventstream source panel
4. Confirm protocol is `Event Hub` and auth is `SAS Key`
5. Confirm `EntityPath` matches source-provided Event Hub name

### "Authentication error from SDK"

Symptom:

```text
Unauthorized / authentication failed / CBS token error
```

Fix:

1. Re-copy SAS key name and key from source settings
2. Ensure no extra spaces in connection string
3. Ensure correct endpoint host and event hub name

### "Eventstream created but still no data"

Fix:

1. Open source settings and verify protocol/auth settings again
2. Check source status is healthy
3. Send a single test event and refresh preview
4. Wait 15-30 seconds for pipeline visibility

---

## 🔐 Security Notes

- Treat SAS key like a password
- Do not commit connection strings to public repos
- Prefer environment variables for local runs

Recommended `.gitignore` additions:

```text
.env
fabric_bridge.py
```

---

## 🎯 Next Steps

After source ingestion is confirmed:

1. Continue to Eventhouse setup
2. Map incoming JSON fields to table columns
3. Build semantic model and app visuals

Next: [Step 4: Setup Eventhouse & KQL](./04-EVENTHOUSE-SETUP.md)
