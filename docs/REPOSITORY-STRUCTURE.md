# 📁 Repository Structure

Complete file listing and organization of the Minecraft RTI GitHub repository.

## 🎯 Quick Navigation

- **Getting Started?** Start with [README.md](../README.md)
- **Want to Replicate?** Use [EXACT-REPLICATION-PROMPT.md](../prompts/EXACT-REPLICATION-PROMPT.md)
- **Want to Customize?** Use [CUSTOM-AGENT-PROMPT-TEMPLATE.md](../prompts/CUSTOM-AGENT-PROMPT-TEMPLATE.md)
- **Setup Confused?** Check [01-INSTALLATION.md](./01-INSTALLATION.md)
- **Issues?** See [TROUBLESHOOTING.md](./TROUBLESHOOTING.md)

---

## 📂 Full Directory Structure

```
minecraft-rti-demo/
│
├── README.md                              ⭐ Start here
│
├── LICENSE                                📜 MIT License
├── .gitignore                             🚫 Git configuration
│
├── 📖 DOCUMENTATION
│   ├── docs/
│   │   ├── 01-INSTALLATION.md            📋 Prerequisites & setup
│   │   ├── 02-MINECRAFT-WAREHOUSE.md    🎮 Build warehouse
│   │   ├── 03-EVENTSTREAM-SETUP.md      🌊 Connect to Fabric
│   │   ├── 04-EVENTHOUSE-SETUP.md       📊 Data warehouse
│   │   ├── 05-SEMANTIC-MODEL.md         📈 Business logic
│   │   ├── 06-FABRIC-APP.md             💻 Dashboard
│   │   ├── TECHNICAL-REFERENCE.md       🔧 Deep dive
│   │   ├── TROUBLESHOOTING.md           🐛 Common issues
│   └── REPOSITORY-STRUCTURE.md           (this file)
│
├── 🤖 COPILOT PROMPTS
│   ├── prompts/
│   │   ├── EXACT-REPLICATION-PROMPT.md       ✅ Copy my project
│   │   ├── CUSTOM-AGENT-PROMPT-TEMPLATE.md   🎨 Build your own
│   │   ├── COPILOT-EXAMPLES.md               💡 Example interactions
│   │   └── PRE-BUILT-SCENARIOS.md            📋 Scenario templates
│   │
│
├── 🐍 PYTHON BACKEND
│   ├── code/
│   │   ├── fabric_bridge.py                  🌉 WebSocket bridge
│   │   ├── warehouse_builder.py              🔨 Warehouse structure
│   │   ├── warehouse_worker.py               👷 Agent simulation
│   │   ├── requirements.txt                  📦 Dependencies
│   │   └── README-PYTHON.md                  📖 Python guide
│   │
│
├── ⚛️  FRONTEND APPLICATION
│   ├── MinecraftApp/
│   │   ├── src/
│   │   │   ├── App.tsx                       🎨 Main component
│   │   │   ├── main.tsx                      🚀 Entry point
│   │   │   ├── global.css                    🎨 Global styles
│   │   │   │
│   │   │   ├── components/
│   │   │   │   ├── auth-gate.component.tsx   🔐 Auth wrapper
│   │   │   │   ├── dashboard.component.tsx   📊 Dashboard
│   │   │   │   ├── metrics-card.component.tsx 📈 KPI cards
│   │   │   │   ├── activity-chart.tsx        📉 Charts
│   │   │   │   └── zone-heatmap.tsx          🔥 Heatmap
│   │   │   │
│   │   │   ├── hooks/
│   │   │   │   ├── use-auth.tsx              🔐 Auth hook
│   │   │   │   ├── use-theme.ts              🎨 Theme hook
│   │   │   │   ├── auth.context.ts           🔐 Auth context
│   │   │   │   ├── theme.context.ts          🎨 Theme context
│   │   │   │   ├── use-semantic-model-query.ts  📊 Data hook
│   │   │   │   └── use-warehouse-metrics.ts     📈 Metrics hook
│   │   │   │
│   │   │   ├── lib/
│   │   │   │   ├── fabric-client.ts          ☁️ Fabric API
│   │   │   │   ├── rayfin-client.ts          📊 Rayfin API
│   │   │   │   ├── utils.ts                  🛠️ Utilities
│   │   │   │   ├── to-data-table.ts          📋 Data transform
│   │   │   │   └── constants.ts              ⚙️ Configuration
│   │   │   │
│   │   │   ├── services/
│   │   │   │   ├── rayfin-auth.service.ts    🔐 Auth service
│   │   │   │   ├── warehouse.service.ts      🏭 Business logic
│   │   │   │   └── analytics.service.ts      📊 Analytics logic
│   │   │   │
│   │   │   ├── test/
│   │   │   │   ├── setup.ts                  🧪 Test setup
│   │   │   │   ├── App.spec.tsx              🧪 App tests
│   │   │   │   ├── to-data-table.spec.ts     🧪 Transform tests
│   │   │   │   └── use-semantic-model-query.spec.ts 🧪 Hook tests
│   │   │   │
│   │   │   └── vite-env.d.ts                 📝 Type definitions
│   │   │
│   │   ├── public/
│   │   │   ├── favicon.ico                   🖼️ Favicon
│   │   │   └── index.html                    📄 Fallback HTML
│   │   │
│   │   ├── scripts/
│   │   │   └── open-fabric-portal.mjs        🚀 Dev helper
│   │   │
│   │   ├── package.json                      📦 Dependencies
│   │   ├── package-lock.json                 🔒 Lock file
│   │   ├── tsconfig.json                     ⚙️ TypeScript config
│   │   ├── tsconfig.node.json                ⚙️ Node TypeScript config\n│   ├── vite.config.ts                     ⚙️ Vite config\n│   ├── vitest.config.ts                    🧪 Test config\n│   ├── eslint.config.js                    ✅ Linter config\n│   ├── tailwind.config.js                  🎨 Tailwind config\n│   ├── fabric.yaml                         ⚙️ Fabric configuration\n│   ├── rayfin/\n│   │   └── rayfin.yml                      ⚙️ Rayfin config\n│   ├── fabric.generated.ts                 🤖 Auto-generated\n│   ├── index.html                          📄 HTML template\n│   ├── components.json                     📋 Component registry\n│   ├── vite-env.d.ts                       📝 Vite types\n│   ├── README.md                           📖 App README\n│   ├── SECURITY.md                         🔒 Security policy\n│   ├── AGENTS.md                           🤖 Agent configuration\n│   ├── CODE_OF_CONDUCT.md                  🤝 Community standards\n│   ├── LICENSE                             📜 License\n│   └── .eslintignore                       🚫 Eslint exclusions\n│\n├── 📊 DATA & CONFIG\n│   ├── warehouse_coordinates.md             🗺️ Zone mapping\n│   ├── event_schema.json                    📋 Event structure\n│   ├── kql_queries.sql                      🔍 KQL templates\n│   └── sample_data.json                     📦 Sample events\n│\n├── 🚀 CI/CD & DEPLOYMENT\n│   ├── .github/\n│   │   ├── workflows/\n│   │   │   ├── build.yml                    🔨 Build pipeline\n│   │   │   ├── test.yml                     🧪 Test pipeline\n│   │   │   └── deploy.yml                   🚀 Deploy pipeline\n│   │   └── ISSUE_TEMPLATE/\n│   │       ├── bug_report.md                🐛 Bug template\n│   │       ├── feature_request.md           ✨ Feature template\n│   │       └── question.md                  ❓ Question template\n│   │\n│   ├── docker/\n│   │   ├── Dockerfile                       🐳 Docker image\n│   │   ├── docker-compose.yml               🐳 Compose config\n│   │   └── .dockerignore                    🚫 Docker excludes\n│   │\n│   └── azure/\n│       ├── deploy.bicep                     ☁️ Infrastructure\n│       ├── deploy.json                      ☁️ ARM template\n│       ├── parameters.json                  ⚙️ Parameters\n│       └── README.md                        📖 Deployment guide\n│\n├── 📝 PROJECT FILES\n│   ├── .gitignore                          🚫 Git configuration\n│   ├── .env.example                        ⚙️ Environment template\n│   ├── CONTRIBUTING.md                     🤝 Contribution guide\n│   ├── CHANGELOG.md                        📝 Version history\n│   ├── ROADMAP.md                          🗺️ Future plans\n│   └── CUSTOMIZATIONS.md                   🎨 Custom variations\n│\n└── 📞 SUPPORT\n    ├── SUPPORT.md                          💬 Support channels\n    ├── SECURITY.md                         🔒 Security policy\n    └── CODE_OF_CONDUCT.md                  🤝 Community standards\n```

---

## 📋 File Descriptions

### Core Documentation

| File | Purpose | Audience |
|------|---------|----------|
| `README.md` | Project overview | Everyone |
| `01-INSTALLATION.md` | Setup guide | First-time users |
| `02-MINECRAFT-WAREHOUSE.md` | Warehouse building | Builders |
| `03-EVENTSTREAM-SETUP.md` | EventStream config | Data engineers |
| `04-EVENTHOUSE-SETUP.md` | Data warehouse | Data engineers |
| `05-SEMANTIC-MODEL.md` | Business logic | Analysts |
| `06-FABRIC-APP.md` | Dashboard dev | Front-end devs |
| `TECHNICAL-REFERENCE.md` | Architecture | Advanced users |
| `TROUBLESHOOTING.md` | Problem solving | Everyone |
| `FAQ.md` | Common questions | Everyone |

### Copilot Prompts

| File | Purpose | Use Case |
|------|---------|----------|
| `EXACT-REPLICATION-PROMPT.md` | Copy this project | Exact replication |
| `CUSTOM-AGENT-PROMPT-TEMPLATE.md` | Build custom agents | Custom scenarios |
| `COPILOT-EXAMPLES.md` | Example interactions | Learning |
| `PRE-BUILT-SCENARIOS.md` | Ready-to-use templates | Quick start |

### Python Code

| File | Purpose | Purpose |
|------|---------|---------|
| `fabric_bridge.py` | WebSocket ↔ EventHub | Core integration |
| `warehouse_builder.py` | Build warehouse | Setup |
| `warehouse_worker.py` | Agent simulation | Data generation |
| `requirements.txt` | Python dependencies | Setup |

### Frontend Code

| Directory | Contains |
|-----------|----------|
| `src/components/` | React components |
| `src/hooks/` | Custom React hooks |
| `src/lib/` | Utility functions |
| `src/services/` | Business logic |
| `src/test/` | Unit tests |

---

## 🔄 File Relationships

```
Graph of dependencies:

README.md (Start here)
├── Installation guide
│   └── 01-INSTALLATION.md
│       ├── Needs Azure setup
│       ├── Needs Python
│       └── Needs Node.js
│
├── Exact copy path
│   └── EXACT-REPLICATION-PROMPT.md
│       ├── Uses warehouse_builder.py
│       ├── Uses warehouse_worker.py
│       └── Uses fabric_bridge.py
│
├── Custom path
│   └── CUSTOM-AGENT-PROMPT-TEMPLATE.md
│       ├── Generates Python code
│       └── Uses fabric_bridge.py
│
└── Full pipeline
    ├── 02-MINECRAFT-WAREHOUSE.md (warehouse_builder.py)
    ├── 03-EVENTSTREAM-SETUP.md (fabric_bridge.py)
    ├── 04-EVENTHOUSE-SETUP.md (KQL queries)
    ├── 05-SEMANTIC-MODEL.md (DAX measures)
    └── 06-FABRIC-APP.md (React components)
```

---

## 🏗️ Development Structure

### For Backend Development

1. Start: `code/fabric_bridge.py`
2. Test: Run WebSocket server
3. Monitor: Check Azure EventHub
4. Debug: Review logs in terminal

### For Data Engineering

1. Start: `04-EVENTHOUSE-SETUP.md`
2. Create: KQL tables
3. Query: Test with sample events
4. Monitor: Check data quality

### For Frontend Development

1. Start: `MinecraftApp/src/App.tsx`
2. Run: `npm run dev`
3. Build: React components
4. Test: Local testing
5. Deploy: `npm run build`

### For Data Scientists

1. Start: `04-EVENTHOUSE-SETUP.md` (KQL queries)
2. Analyze: Real data patterns
3. Create: `05-SEMANTIC-MODEL.md` (DAX measures)
4. Visualize: `06-FABRIC-APP.md` (Dashboard)

---

## 📦 Dependencies

### Python Packages

```
websockets>=12.0
azure-eventhub>=5.10
```

### Node Packages

See `MinecraftApp/package.json` for full list:
- React 19+
- TypeScript 5.7+
- Tailwind CSS 4.2+
- Rayfin (Fabric integration)
- Vite (Build tool)

---

## 🔑 Key Concepts by File

| Concept | File |
|---------|------|
| Real-time streaming | `03-EVENTSTREAM-SETUP.md` |
| Event schema | `04-EVENTHOUSE-SETUP.md` |
| Data aggregation | `04-EVENTHOUSE-SETUP.md` |
| Business logic | `05-SEMANTIC-MODEL.md` |
| Live dashboard | `06-FABRIC-APP.md` |
| Architecture | `TECHNICAL-REFERENCE.md` |
| Troubleshooting | `TROUBLESHOOTING.md` |

---

## 📥 Typical User Journeys

### Journey 1: Exact Replication
1. Read `README.md`
2. Read `01-INSTALLATION.md`
3. Follow `EXACT-REPLICATION-PROMPT.md`
4. Complete `02-MINECRAFT-WAREHOUSE.md`
5. Complete `03-EVENTSTREAM-SETUP.md` → `06-FABRIC-APP.md`

### Journey 2: Custom Scenario
1. Read `README.md`
2. Read `01-INSTALLATION.md`
3. Follow `CUSTOM-AGENT-PROMPT-TEMPLATE.md`
4. Follow `02-MINECRAFT-WAREHOUSE.md`
5. Follow `03-EVENTSTREAM-SETUP.md` → `06-FABRIC-APP.md`

### Journey 3: Deep Learning
1. Read `README.md`
2. Read `TECHNICAL-REFERENCE.md`
3. Read code files: `fabric_bridge.py`, `warehouse_worker.py`
4. Review `04-EVENTHOUSE-SETUP.md` (KQL)
5. Review `05-SEMANTIC-MODEL.md` (DAX)
6. Review `MinecraftApp/src/` (React)

---

## 🎯 Search Guide

**Looking for...**

- Setup help? → `01-INSTALLATION.md`
- How to build warehouse? → `02-MINECRAFT-WAREHOUSE.md`
- EventStream problems? → `03-EVENTSTREAM-SETUP.md` & `TROUBLESHOOTING.md`
- KQL examples? → `04-EVENTHOUSE-SETUP.md`
- DAX measures? → `05-SEMANTIC-MODEL.md`
- React components? → `MinecraftApp/src/components/`
- Copilot prompts? → `prompts/` folder
- Architecture details? → `TECHNICAL-REFERENCE.md`
- Error solutions? → `TROUBLESHOOTING.md`
- FAQ? → `FAQ.md`

---

## 📈 Recommended Learning Path

1. **Beginner** (2 hours)
   - `README.md` (10 min)
   - `01-INSTALLATION.md` (30 min)
   - `EXACT-REPLICATION-PROMPT.md` (60 min)
   - `02-MINECRAFT-WAREHOUSE.md` (20 min)

2. **Intermediate** (4 hours)
   - All of Beginner
   - `03-EVENTSTREAM-SETUP.md` (30 min)
   - `04-EVENTHOUSE-SETUP.md` (45 min)
   - `05-SEMANTIC-MODEL.md` (45 min)
   - `06-FABRIC-APP.md` (60 min)

3. **Advanced** (8 hours)
   - All of Intermediate
   - `TECHNICAL-REFERENCE.md` (90 min)
   - Code review: `fabric_bridge.py`, `warehouse_worker.py`
   - Code review: `MinecraftApp/src/` (120 min)
   - `TROUBLESHOOTING.md` (30 min)

---

**Ready to start?** → [README.md](../README.md)
