# 🆘 Troubleshooting Guide

Common issues and solutions for the Minecraft RTI project.

## 🔧 Quick Diagnostics

### 1. Test WebSocket Connection

```bash
# Terminal: Check if WebSocket server running
netstat -ano | findstr :3000  # Windows
lsof -i :3000                 # macOS/Linux

# Should show Python process listening
```

### 2. Test Minecraft Chat

In Minecraft, type:
```
FABRIC_EVENT|{"test":"message"}
```

Check terminal for:
```
Event received: FABRIC_EVENT|{"test":"message"}
```

### 3. Test EventHub Connection

```python
# Run this in Python terminal
from azure.eventhub import EventHubProducerClient, EventData

connection_str = "Your connection string"
producer = EventHubProducerClient.from_connection_string(connection_str)
with producer:
    producer.send_batch([EventData("Test")])
    print("✅ EventHub connection successful")
```

---

## 📋 Installation Issues

### Python Not Found

**Error:**
```
'python' is not recognized as an internal or external command
```

**Solutions:**
1. **Verify Installation**
   ```bash
   python --version
   ```

2. **Add to PATH (Windows)**
   - Settings → System → About → Advanced system settings
   - Environment Variables → Path
   - Add: `C:\Users\[YourName]\AppData\Local\Programs\Python\Python311`
   - Restart terminal

3. **Reinstall Python**
   - Download from [python.org](https://python.org)
   - **Check "Add Python to PATH"**
   - Install

### Node.js/npm Not Found

**Error:**
```
'npm' is not recognized as an internal or external command
```

**Solutions:**
1. **Verify Installation**
   ```bash
   npm --version
   ```

2. **Reinstall Node.js**
   - Download from [nodejs.org](https://nodejs.org)
   - **Check "Add to PATH"**
   - Install

3. **Restart Terminal**
   - Close and reopen terminal
   - Environment variables take effect after restart

### Minecraft Won't Start

**Error:**
```
Minecraft application fails to launch
```

**Solutions:**
1. **Check System Requirements**
   - Windows 10/11 build 19041+
   - macOS 12+

2. **Reinstall Minecraft**
   - Uninstall from Microsoft Store
   - Reinstall from Microsoft Store

3. **Check Disk Space**
   - Need ~2-3 GB free
   - Check: `Disk Management` (Windows) or `Disk Utility` (macOS)

---

## 🌐 Connection Issues

### Minecraft Can't Connect to WebSocket

**Error (in Minecraft):**
```
/connect localhost:3000
Connection failed
```

**Diagnosis:**
```bash
# Check if server is running
netstat -ano | findstr :3000

# If nothing found, server is not running
```

**Solutions:**

1. **Start WebSocket Server**
   ```bash
   cd minecraft-rti-demo
   python fabric_bridge.py
   
   # Should output:
   # WebSocket server listening on ws://localhost:3000
   ```

2. **Check Port 3000**
   ```bash
   # Find what's using port 3000
   netstat -ano | findstr :3000
   
   # Kill the process if needed (Windows)
   taskkill /PID [PID] /F
   
   # Or use different port in fabric_bridge.py:
   PORT = 3001
   ```

3. **Check Firewall**
   - Windows Defender Firewall → Advanced Settings
   - Inbound Rules → New Rule
   - Allow Python.exe on port 3000
   - Apply

4. **Restart Both**
   ```bash
   # Kill server
   Ctrl+C in terminal
   
   # Restart server
   python fabric_bridge.py
   
   # Retry in Minecraft
   /connect localhost:3000
   ```

### Connection Drops Randomly

**Error:**
```
Connected, then randomly disconnects
```

**Solutions:**
1. **Increase Timeout**
   ```python
   # In fabric_bridge.py, change:
   async with timeout(60):  # Increase from 30
   ```

2. **Check Firewall Settings**
   - Some firewalls drop idle connections
   - Add keep-alive heartbeat

3. **Monitor Network**
   - Check internet stability
   - Run: `ping 8.8.8.8` repeatedly
   - If packets drop, network issue

---

## ☁️ Azure & Fabric Issues

### EventHub Connection String Invalid

**Error:**
```
Exception: Invalid connection string
```

**Solutions:**
1. **Verify Connection String**
   ```python
   # Check format:
   # Endpoint=sb://[NAMESPACE].servicebus.windows.net/;
   # SharedAccessKeyName=RootManageSharedAccessKey;
   # SharedAccessKey=[KEY];
   # EntityPath=[EVENT_HUB_NAME]
   ```

2. **Get Correct String**
   - Azure Portal → Event Hubs
   - Your namespace → Shared access policies
   - RootManageSharedAccessKey → Copy connection string

3. **Verify No Spaces**
   ```python
   # Wrong:
   connection_str = "Endpoint=sb://... ; SharedAccessKey=..."
   
   # Right:
   connection_str = "Endpoint=sb://...;SharedAccessKey=..."
   ```

### Events Not Reaching EventHub

**Error:**
```
Events sent but nothing in EventHub
```

**Solutions:**
1. **Verify Event Format**
   ```python
   # Must have FABRIC_EVENT| prefix
   # Must be valid JSON
   
   # Wrong:
   FABRIC_EVENT|{incomplete json
   
   # Right:
   FABRIC_EVENT|{"event_type":"test","agent_name":"worker"}
   ```

2. **Check Event Size**
   ```python
   # Payload must be < 1 MB
   # Typical event: 200-500 bytes
   
   import json
   event = {"event_type": "test"}
   size = len(json.dumps(event).encode('utf-8'))
   print(f"Event size: {size} bytes")
   ```

3. **Check Throughput**
   - Azure Portal → EventHub → Metrics
   - Look for \"Incoming Requests\"
   - Should show recent spikes

4. **Verify Credentials**
   ```python
   # Test directly
   from azure.eventhub import EventHubProducerClient
   
   try:
       client = EventHubProducerClient.from_connection_string(CONNECTION_STRING)
       print("✅ Connection successful")
   except Exception as e:
       print(f"❌ Connection failed: {e}")
   ```

### Fabric Workspace Not Accessible

**Error:**
```
Cannot access Fabric workspace
```

**Solutions:**
1. **Verify Workspace Exists**
   - Go to [fabric.microsoft.com](https://fabric.microsoft.com)
   - Sign in with correct Microsoft account
   - Check workspace appears in list

2. **Check Permissions**
   - You should have Editor or Admin role
   - Ask workspace owner if not

3. **Try Incognito**
   - Open new incognito window
   - Sign in again
   - Sometimes fixes cache issues

---

## 📊 Data Pipeline Issues

### No Data in Eventhouse

**Error:**
```
warehouse_events table exists but is empty
```

**Diagnosis:**
1. **Check EventStream Receiving**
   ```
   Go to EventStream → Preview
   Should show events flowing in real-time
   ```

2. **Check Event Format**
   ```kql
   // In Eventhouse
   warehouse_events | count
   // Should be > 0
   ```

**Solutions:**
1. **Verify Events Are Flowing**
   - In fabric_bridge.py terminal
   - Should see: \"Event received: warehouse_activity...\"
   - If not, review \"Connection Issues\" section

2. **Check Timestamp Format**
   ```python
   # Must be ISO 8601
   import datetime
   timestamp = datetime.datetime.utcnow().isoformat() + \"Z\"
   print(timestamp)  # 2024-01-15T10:30:45.123456Z
   ```

3. **Wait for Ingestion Delay**
   - Events take 2-5 minutes to appear
   - Don't check immediately
   - Wait 5+ minutes then try again

### Query Returns No Results

**Error:**
```kql
warehouse_events | count
// Result: 0
```

**Solutions:**
1. **Check Table Name**
   ```kql
   // Verify table exists
   .show tables
   ```

2. **Check Timestamp Filter**
   ```kql
   // Don't filter too old data
   warehouse_events
   | where timestamp > now(-30d)  // Check last 30 days
   | count
   ```

3. **Verify Data Type**
   ```kql
   // Check column types
   warehouse_events
   | getschema
   ```

4. **Check Event Structure**
   - Verify JSON has correct field names
   - Case-sensitive in some tools
   - Use `.show table warehouse_events cslschema` to verify

---

## ⚡ Performance Issues

### Dashboard Loading Slowly

**Error:**
```
Fabric App takes 10+ seconds to load
```

**Solutions:**
1. **Check Network Speed**
   ```bash
   ping fabric.microsoft.com
   # Should be < 100ms
   ```

2. **Check Browser Performance**
   - Open DevTools (F12)
   - Check Network tab for slow requests
   - Check Console for errors

3. **Optimize Queries**
   - Add timestamp filters
   - Limit data ranges
   - Cache results client-side

4. **Check Semantic Model Refresh**
   - Workspace → Semantic Models
   - Your model → Refresh history
   - Should be < 1 minute

### WebSocket Server High CPU

**Error:**
```
fabric_bridge.py using 50%+ CPU
```

**Solutions:**
1. **Reduce Event Frequency**
   - In warehouse_worker.py, increase SLEEP_TIME
   ```python
   SLEEP_TIME = 10  # Was 5 seconds, now 10
   ```

2. **Batch Events**
   ```python
   # Instead of sending every event
   # Collect 10 events, send batch
   ```

3. **Monitor Memory**
   ```bash
   # Windows Task Manager → Performance
   # macOS Activity Monitor
   
   # If using > 500 MB, restart server
   ```

---

## 🐛 Code Issues

### Python Syntax Errors

**Error:**
```
IndentationError: unexpected indent
```

**Solutions:**
1. **Check Indentation**
   - Use 4 spaces (not tabs)
   - Consistent throughout file

2. **Validate Syntax**
   ```bash
   python -m py_compile fabric_bridge.py
   # Should output nothing if OK
   ```

### Minecraft Code Builder Errors

**Error:**
```
Code fails when running in Minecraft
```

**Solutions:**
1. **Test in IDE First**
   - Paste Python code in VS Code
   - Run with Python interpreter
   - Fix errors before Minecraft

2. **Check API Methods**
   - `agent.say()` - Chat message
   - `blocks.setBlock()` - Block manipulation
   - `player.getTilePos()` - Get position

3. **Limited Libraries**
   - Can't use: pandas, numpy, requests, websockets
   - Can use: math, time, random, json (basic)

---

## 🔄 Integration Issues

### Semantic Model Not Syncing

**Error:**
```
Changes in Eventhouse don't appear in model
```

**Solutions:**
1. **Manual Refresh**
   - Workspace → Semantic Models
   - Right-click model → Refresh
   - Wait 1-2 minutes

2. **Check Refresh Schedule**
   - Model settings → Refresh
   - Verify daily/hourly refresh enabled

3. **Verify Connection**
   - Model → Edit → Check connection to Eventhouse
   - Re-establish if needed

### Fabric App Not Showing Data

**Error:**
```
Dashboard loads but shows no data
```

**Solutions:**
1. **Check Browser Console**
   - F12 → Console tab
   - Look for JavaScript errors
   - Fix errors in code

2. **Verify Semantic Model has Data**
   - Test query in Semantic Model
   - Create simple measure: `COUNT(warehouse_events[timestamp])`
   - Should show > 0

3. **Check Authentication**
   - Sign in to Fabric
   - Verify you can access workspace
   - Verify you can access semantic model

---

## 📝 Debugging Tips

### Enable Verbose Logging

**Python:**
```python
import logging
logging.basicConfig(level=logging.DEBUG)

# In fabric_bridge.py
logger = logging.getLogger(__name__)
logger.debug(f\"Event: {event_data}\")
```

**Browser:**
```
F12 → Console → Type in console
```

### Save Events Locally

```python
# In fabric_bridge.py
with open('events.log', 'a') as f:
    f.write(f\"{datetime.now()} - {event_data}\\n\")
```

### Test Each Component

1. **Python alone:**
   ```bash
   python fabric_bridge.py
   # Should start without errors
   ```

2. **Add Minecraft:**
   ```
   /connect localhost:3000
   # Should connect
   ```

3. **Add EventHub:**
   - Send test event
   - Check Azure Portal

4. **Add Eventhouse:**
   - Query for events
   - Check data appears

---

## 🚨 Critical Errors

### Out of Memory

**Error:**
```
MemoryError or "out of memory"
```

**Solutions:**
1. **Reduce Data Range**
   - Query only last 1 day
   - Reduce KQL result sets

2. **Restart Application**
   ```bash
   # Kill Python process
   Ctrl+C
   
   # Restart
   python fabric_bridge.py
   ```

3. **Check System Memory**
   ```bash
   # Windows
   systeminfo | find \"Total Physical Memory\"
   
   # macOS
   vm_stat
   ```

### Database Locked

**Error:**
```
Database connection error
```

**Solutions:**
1. **Wait and Retry**
   - Wait 30 seconds
   - Retry operation

2. **Close Other Connections**
   - Close other Fabric tabs
   - Sign out and back in

3. **Contact Fabric Support**
   - If persists > 1 hour
   - May be platform issue

---

## 📞 Still Stuck?

1. **Check Documentation**
   - [FAQ.md](./FAQ.md)
   - [TECHNICAL-REFERENCE.md](./TECHNICAL-REFERENCE.md)

2. **Review Logs**
   - fabric_bridge.py terminal output
   - Browser console (F12)
   - Event Hubs metrics

3. **Test Incrementally**
   - Verify each component separately
   - Add pieces one by one
   - Identify which step fails

4. **Ask for Help**
   - Check GitHub Issues
   - Create new Issue with:
     - Error message
     - Steps to reproduce
     - Screenshots/logs
     - System info (OS, versions)

---

**Still need help?** Check [FAQ.md](./FAQ.md) or create a GitHub Issue
