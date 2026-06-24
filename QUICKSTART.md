# 🚀 Quick Start Guide

Get up and running in 90 minutes!

## ⚡ 5-Minute Overview

```
Minecraft Education
        ↓
    Events
        ↓
WebSocket Bridge (Python)
        ↓
Azure EventHub
        ↓
Fabric EventStream
        ↓
Eventhouse (KQL)
        ↓
Semantic Model
        ↓
Fabric App (React)
        ↓
Live Dashboard
```

---

## ⏱️ 90-Minute Quickstart

### 10 min: Prerequisites
- [ ] Python 3.10+ installed
- [ ] Node.js 18+ installed
- [ ] Minecraft Education launched
- [ ] Fabric workspace created
- [ ] Azure EventHub created

### 15 min: Get Code
```bash
git clone https://github.com/microsoft/minecraft-rti-demo.git
cd minecraft-rti-demo
pip install -r code/requirements.txt
cd MinecraftApp && npm install && cd ..
```

### 5 min: Configure
```bash
# Update fabric_bridge.py with your EventHub connection string
# Update MinecraftApp/fabric.yaml with your workspace ID
```

### 10 min: Build Warehouse
1. Open Minecraft
2. Create flat world
3. Press 'C' for Code Builder
4. Create new Python project
5. Copy `code/warehouse_builder.py`
6. Run code (3-4 min to build)

### 15 min: Connect EventStream
1. Start WebSocket bridge:
   ```bash
   python code/fabric_bridge.py
   ```
2. In Minecraft:
   ```
   /connect localhost:3000
   ```
3. Test event:
   ```
   FABRIC_EVENT|{"test":"event"}
   ```
4. Verify in EventHub (Azure Portal)

### 15 min: Setup Eventhouse
1. Create Eventhouse in Fabric
2. Connect EventStream to EventHub
3. Create `warehouse_events` table
4. Run test query

### 10 min: Create Semantic Model
1. Create semantic model in Fabric
2. Connect to Eventhouse
3. Add measures:
   - Total Items = SUM(...)
   - Avg Efficiency = AVG(...)
   - Event Count = COUNT(...)

### 15 min: Deploy Fabric App
1. Run app:
   ```bash
   cd MinecraftApp
   npm run dev
   ```
2. Open http://localhost:5173
3. Build dashboard with React components
4. Deploy to Fabric

### 10 min: Test Everything
1. Run warehouse worker
2. Watch events flow
3. Check Eventhouse for data
4. View real-time dashboard

---

## 🎯 Choose Your Path

### Path A: Exact Replication (1.5 hours)
1. Follow Quickstart steps above
2. Use provided code as-is
3. Run warehouse worker script
4. Done!

### Path B: Custom Scenario (2 hours)
1. Modify warehouse zones
2. Use Copilot prompt to generate worker
3. Customize dashboard
4. Deploy your version

### Path C: Deep Learning (4-6 hours)
1. Follow all steps
2. Study code files
3. Review TECHNICAL-REFERENCE.md
4. Make advanced customizations

---

## 📞 Instant Help

| Issue | Solution |
|-------|----------|
| Can't connect to Minecraft | Start `fabric_bridge.py` |
| No data in Eventhouse | Wait 5 min for ingestion |
| Dashboard won't load | Check browser console (F12) |
| Python errors | Check TROUBLESHOOTING.md |
| Copilot code won't paste | Clear Code Builder, paste again |

---

## ✅ Verification Checklist

- [ ] Python dependencies installed
- [ ] Node packages installed
- [ ] Minecraft warehouse built
- [ ] WebSocket bridge running
- [ ] Events in EventHub
- [ ] Data in Eventhouse
- [ ] Semantic model created
- [ ] Dashboard deployed
- [ ] Real-time data flowing

---

## 📊 Expected Results

After 90 minutes, you should have:

✅ Minecraft warehouse with 6 zones
✅ Events flowing: Minecraft → EventHub → Eventhouse
✅ Real-time KQL queries returning data
✅ Semantic model with 5+ measures
✅ Live dashboard showing:
   - Total items processed
   - Average efficiency
   - Active zones
   - Real-time activity table

---

## 🎓 Next: 90-Minute Expert Path

Once basic setup works:
1. Add custom zones
2. Create advanced analytics
3. Build ML predictions
4. Create team dashboards
5. Deploy to production

---

## 💡 Pro Tips

✅ Record your setup with screen capture
✅ Take screenshots at key milestones  
✅ Keep terminal output for debugging
✅ Test each component individually
✅ Save workspace IDs for reference

---

**Start now!** → [INSTALLATION.md](./docs/01-INSTALLATION.md)
