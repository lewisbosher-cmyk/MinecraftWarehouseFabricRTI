# 🏭 Minecraft Real-Time Intelligence (RTI) Demo

A comprehensive guide to building a real-time data intelligence solution using **Minecraft Education Edition** as a data simulation engine, connected to **Microsoft Fabric** for analytics and visualization.

This project demonstrates:
- 🎮 **Minecraft** as a real-world simulation environment
- 🌊 **Fabric Eventstream** for real-time data ingestion
- 📊 **Eventhouse** for data warehousing
- 📈 **Semantic Models** for business logic
- 💻 **Fabric Apps** for interactive dashboards

## 📋 Quick Start

1. **[Installation & Setup](./docs/01-INSTALLATION.md)** - Environment prerequisites
2. **[Minecraft Warehouse Build](./docs/02-MINECRAFT-WAREHOUSE.md)** - Create your warehouse
3. **[EventStream Configuration](./docs/03-EVENTSTREAM-SETUP.md)** - Connect to Fabric
4. **[Eventhouse & Data Pipeline](./docs/04-EVENTHOUSE-SETUP.md)** - Data warehousing
5. **[Semantic Model](./docs/05-SEMANTIC-MODEL.md)** - Business logic layer
6. **[Fabric App Development](./docs/06-FABRIC-APP.md)** - Build dashboards

## 🎯 Project Overview

### Architecture Flow

```
Minecraft Education Edition
         ↓
    WebSocket Server (Python)
         ↓
  Fabric Eventstream
         ↓
   Eventhouse (KQL Tables)
         ↓
   Semantic Model
         ↓
  Fabric App (React/TypeScript)
```

### Key Components

| Component | Purpose | Technology |
|-----------|---------|-----------|
| **Minecraft Warehouse** | Data source simulation | Minecraft Education Edition |
| **Fabric Bridge** | WebSocket-to-EventStream | Python (asyncio, websockets) |
| **EventStream** | Real-time data ingestion | Azure Fabric EventStream |
| **Eventhouse** | Data warehouse | Fabric Eventhouse (KQL) |
| **Semantic Model** | Analytics data model | Fabric Semantic Models |
| **Fabric App** | Interactive dashboard | React/TypeScript/Rayfin |

## 🚀 For Different Use Cases

### 📋 Want to Replicate This Exact Project?
→ **[Use the Exact Replication Prompt](./prompts/EXACT-REPLICATION-PROMPT.md)**
- Creates an exact copy of the warehouse worker scenario
- 10-15 minutes setup time
- Perfect for learning the full pipeline

### 🎨 Want to Create Your Own Custom Scenario?
→ **[Use the Custom Agent Prompt Template](./prompts/CUSTOM-AGENT-PROMPT-TEMPLATE.md)**
- Customize the Minecraft agent behavior
- Define your own data scenarios
- 5-10 minutes customization
- Endless possibilities

### 🧑‍💻 Want Deep Technical Details?
→ **[Architecture & Technical Documentation](./docs/TECHNICAL-REFERENCE.md)**
- Complete system architecture
- Data schemas and models
- API references
- Troubleshooting guide

## 📚 Documentation Structure

```
docs/
├── 01-INSTALLATION.md              # Prerequisites & environment setup
├── 02-MINECRAFT-WAREHOUSE.md       # Building the Minecraft warehouse
├── 03-EVENTSTREAM-SETUP.md         # Configuring Fabric EventStream
├── 04-EVENTHOUSE-SETUP.md          # Setting up Eventhouse & KQL
├── 05-SEMANTIC-MODEL.md            # Creating semantic models
├── 06-FABRIC-APP.md                # Building the Fabric App
└── TROUBLESHOOTING.md              # Common issues & solutions

prompts/
├── CUSTOM-AGENT-PROMPT-TEMPLATE.md # Template for custom scenarios
└── EXACT-REPLICATION-PROMPT.md     # Exact copy prompt

code/
├── fabric_bridge.py                # Python bridge (Minecraft ↔ EventStream)
├── warehouse_builder.py            # Minecraft warehouse builder
├── warehouse_worker.py             # Warehouse worker agent
└── fabric-app/                     # React/TypeScript Fabric App
    ├── src/
    ├── package.json
    └── ... (full app structure)
```

## ⚡ Quick Requirements

- **Minecraft Education Edition** (with Code Builder)
- **Python 3.10+** 
- **Node.js 18+**
- **Microsoft Fabric** workspace (free or paid)
- **Azure Subscription** (for EventHub)

## 🎓 Learning Outcomes

By completing this project, you'll learn:
- ✅ Real-time data simulation with Minecraft
- ✅ Event-driven architectures
- ✅ Fabric EventStream integration
- ✅ KQL (Kusto Query Language) for data analysis
- ✅ Semantic models and data governance
- ✅ Building analytics-ready Fabric Apps
- ✅ GitHub Copilot prompt engineering for code generation

## 🤝 Contributing

This is a demonstration project. Feel free to fork, customize, and share your variations!

### Share Your Customizations
If you create interesting variations:
1. Fork this repository
2. Document your changes in `CUSTOMIZATIONS.md`
3. Submit a pull request

## 🆘 Support

- **Issues?** Check [TROUBLESHOOTING.md](./docs/TROUBLESHOOTING.md)

## 🌟 Credits

Created as a Microsoft Data CSA demonstration showcasing:
- Real-time intelligence capabilities in Fabric
- Innovative data visualization approaches
- Integration between gaming platforms and enterprise analytics

---

**Ready to get started?** → [Start with Installation](./docs/01-INSTALLATION.md)
