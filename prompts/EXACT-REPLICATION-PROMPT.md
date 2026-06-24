# 📋 Exact Replication Prompt for GitHub Copilot

Use this prompt to create an **exact replica** of the warehouse worker scenario from this project. This will generate the complete Minecraft Code Builder script that matches the original implementation.

## 🚀 How to Use

1. **Copy the entire prompt** below (everything between the dashed lines)
2. **Open GitHub Copilot Chat** in VS Code (Ctrl+Shift+I)
3. **Paste the prompt**
4. **Run it** - Copilot will generate the complete code
5. **Copy the generated code** and paste into Minecraft Code Builder
6. **Execute** in your Minecraft Education Edition environment

---

## 📌 EXACT REPLICATION PROMPT

```
I'm creating a Minecraft warehouse worker agent that simulates a warehouse 
logistics operation. This is a real-world event simulation for data pipeline testing.

WAREHOUSE STRUCTURE:
The warehouse has exactly these zones:
- Loading Bay: minX=102, maxX=118, minY=4, maxY=12, minZ=102, maxZ=116
- Storage Area A: minX=122, maxX=158, minY=4, maxY=12, minZ=102, maxZ=128  
- Storage Area B: minX=122, maxX=158, minY=4, maxY=12, minZ=130, maxZ=144
- Packing Station: minX=102, maxX=118, minY=4, maxY=12, minZ=118, maxZ=128
- Forbidden Zone: minX=102, maxX=118, minY=4, maxY=12, minZ=130, maxZ=144
- Control Office: minX=160, maxX=170, minY=4, maxY=12, minZ=102, maxZ=114

AGENT BEHAVIOR:
The warehouse_worker agent should:

1. Be triggered with the command: "run_shift"
2. Perform these operations in sequence (repeat cycling through them):
   a) Pick items from Storage Area A and move them to Packing Station
   b) Move packed items from Packing Station to Loading Bay
   c) Move new stock from Loading Bay to Storage Area B
   d) Travel randomly within the warehouse to simulate realistic work patterns

3. Track these metrics continuously:
   - items_processed: Running count of items handled
   - zone_transitions: Number of times moving between zones
   - efficiency_score: Calculated as (items_processed / time_elapsed) * 100
   - current_zone: Current agent location

4. Every time the agent does anything, send an event with this exact format via agent chat with prefix "FABRIC_EVENT|":

{
  "event_type": "<event_type>",
  "agent_name": "warehouse_worker", 
  "location": "<current_zone_name>",
  "timestamp": "<current_iso_timestamp>",
  "items_processed": <number>,
  "zone_transitions": <number>,
  "efficiency_score": <number>,
  "action": "<action_performed>"
}


5. Can be stopped with the command: "stop_shift"

IMPLEMENTATION REQUIREMENTS:
- Use proper Python syntax for Minecraft Code Builder
- Include the agent.say() method to broadcast events
- Add try/except for error handling
- Include movement animation with agent.move()
- Track real simulation time
- Generate realistic random variations in metrics
- Include detailed comments explaining each section
- Make events continuous throughout the shift
- Support multi-minute shifts without crashing

Generate the complete, working Python script for Minecraft Code Builder.
```

---

## 📥 Step-by-Step Integration

### Step 1: Generate the Code (2 minutes)
1. Open VS Code with this project
2. Open **Copilot Chat** (Ctrl+Shift+I)
3. Paste the prompt above
4. Wait for Copilot to generate complete code
5. Copy the entire generated script

### Step 2: Prepare Minecraft (3 minutes)
1. Launch **Minecraft Education Edition**
2. Create a new **Flat World**
3. Name it: "Warehouse RTI Demo"
4. Open **Code Builder** (Press 'C')
5. Create a new Python project

### Step 3: Set Up Warehouse (5 minutes)
1. Paste and run [warehouse_builder.py](../code/warehouse_builder.py)
   - This creates the exact warehouse structure
   - All zones are color-coded and labeled
   - Takes ~3-4 minutes to build

### Step 4: Add the Worker Agent (2 minutes)
1. Paste the generated worker script into Code Builder
2. Run the code (this initializes the agent)

### Step 5: Connect to Fabric EventStream (5 minutes)
1. In a separate terminal, run:
   ```bash
   python fabric_bridge.py
   ```
   - This starts the WebSocket server
   - Listens on localhost:3000
   - Ready to forward events to your EventStream

2. In Minecraft chat, type:
   ```
   /connect localhost:3000
   ```
   - This connects Minecraft to the bridge

### Step 6: Start the Simulation (1 minute)
1. In Minecraft chat, type:
   ```
   run_shift
   ```
2. Watch the agent work and events flow
3. Check your Fabric EventStream for incoming events

### Step 7: Monitor the Pipeline
1. Open **Fabric Eventstream** console
2. Verify events arriving
3. Check event format and JSON parsing
4. Monitor the warehouse scene in Minecraft

---

## 🎯 Expected Behavior

### Minecraft View
- Agent moves between warehouse zones
- Items appear to be picked/packed/moved
- Zone capacity indicators change
- Chat shows real-time status updates

### EventStream View
- New events arriving
- JSON events with warehouse_activity type
- Occasional zone_capacity_alert events
- Metrics incrementing realistically

### Terminal Output
- fabric_bridge.py shows: "Event received: warehouse_activity"
- WebSocket connections logged
- Event counts incrementing
- Errors (if any) logged for troubleshooting

---

## 📊 Data Flow Verification

After the shift starts, verify each step:

1. **Minecraft → WebSocket** ✅
   - Check fabric_bridge.py terminal for "Connection received"
   - See events logged in real-time

2. **WebSocket → EventHub** ✅
   - Check Fabric EventStream dashboard
   - See events in the live data view
   - Verify JSON structure is correct

3. **EventHub → KQL Table** ✅
   - Run query in Eventhouse:
   ```kql
   raw_warehouse_events
   | where event_type == "warehouse_activity"
   | take 100
   ```
   - Should see your recent events

4. **KQL → Semantic Model** ✅
   - Verify model synced with EventStream
   - Check table refresh is working

5. **Semantic Model → Fabric App** ✅
   - Dashboard updates with real-time data
   - Visualizations show warehouse activity

---

## ⏱️ Timing & Duration

**Recommended shift duration:**
- **Test run**: 30 seconds (quick verification)
- **Full demo**: 5-10 minutes (good data for visualization)
- **Extended demo**: 30+ minutes (trend analysis and capacity patterns)

**Stop the shift:**
```
stop_shift
```

---

## 🔧 Customization After Replication

Once you have the exact setup working, you can customize:

### Add More Metrics
```python
# In the event JSON, add:
"items_by_type": count_by_type(),
"worker_location_history": track_path(),
```

### Add More Zones
```python
# Extend ZONES dict with new areas
# Create new section in warehouse_builder.py
```

### Add Advanced Analytics
```python
# Add to semantic model:
# - Heatmaps by zone
# - Efficiency trends
# - Bottleneck detection
```

---

## 🐛 Troubleshooting

### Copilot Code Generation Issues

**Q: Generated code has import errors**
```
A: Minecraft Code Builder doesn't support all Python libraries.
   Make sure code uses only:
   - agent module (provided in Code Builder)
   - math, time, random (standard library)
   - No requests, pandas, numpy, etc.
```

**Q: Code doesn't run in Minecraft**
```
A: Check:
   1. No syntax errors - paste in Python IDE first
   2. All agent methods exist: agent.say(), agent.move(), agent.getTilePos()
   3. No indentation issues
   4. Chat messages use agent.say(message)
```

**Q: Events don't appear in EventStream**
```
A: Verify:
   1. fabric_bridge.py is running
   2. /connect localhost:3000 executed in Minecraft
   3. Events have "FABRIC_EVENT|" prefix
   4. JSON is valid
```

### Data Pipeline Issues

**Q: Events arrive but don't parse correctly**
```
A: Check KQL table mapping:
   - event_type field exists
   - agent_name is correct spelling
   - timestamp is ISO 8601 format
   - All numeric fields are numbers (not strings)
```

**Q: Dashboard shows no data**
```
A: Verify:
   1. Semantic model refreshed
   2. Tables have rows (check EventhouseQuery)
   3. Dashboard measures use correct columns
   4. Event type filter matches your event_type value
```

---

## 📈 What You'll Learn

By completing this exact replication:

✅ **Minecraft Education Edition** basics and Code Builder
✅ **Real-time event simulation** techniques
✅ **WebSocket architecture** for event streaming
✅ **Fabric EventStream** configuration
✅ **KQL (Kusto Query Language)** for data querying
✅ **Semantic Models** design
✅ **Event-driven data pipelines**
✅ **Real-time analytics dashboards**

---

## 📚 Next Steps After Replication

1. **Verify the pipeline** - All data flows end-to-end
2. **Explore semantic model** - Understand the data structure
3. **Build custom dashboards** - Try different visualizations
4. **Customize the agent** - Add your own metrics
5. **Create custom scenarios** - Use the template prompt instead

---

## 🎓 Learning Resources

- [Minecraft Education Edition Docs](https://docs.microsoft.com/en-us/minecraft/creator/)
- [Fabric EventStream Docs](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/eventstream/eventstream-overview)
- [KQL Query Reference](https://learn.microsoft.com/en-us/kusto/query/)
- [Fabric Apps Development](https://learn.microsoft.com/en-us/fabric/dev-gate/fabric-apps/overview)

---

**💡 Tip**: Record your shift performance to create a video demo!

```bash
# Use OBS or Windows Game Bar to record while running:
# 1. Start recording (Win+Alt+R)
# 2. Run shift in Minecraft
# 3. Stop shift after 5-10 minutes
# 4. Export video for presentation
```

---

**Ready to replicate?** Start with Step 1: [Generate the Code](#step-1-generate-the-code-2-minutes)

**Questions?** See [TROUBLESHOOTING.md](../docs/TROUBLESHOOTING.md) or [FAQ.md](../docs/FAQ.md)
