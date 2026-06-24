# 1️⃣ Installation & Environment Setup

Complete guide to preparing your environment for the Minecraft RTI project.

## 📋 Prerequisites Checklist

- [ ] Windows 10/11 or macOS 12+
- [ ] Admin access (for software installation)
- [ ] Microsoft Fabric workspace (Free or Premium)
- [ ] Azure subscription (for EventHub)
- [ ] Internet connection (5+ Mbps recommended)

---

## 🎮 Step 1: Install Minecraft Education Edition

### Windows

1. **Open Microsoft Store**
   - Search for "Minecraft Education Edition"
   - Click **Get**
   - Wait for installation (~2-3 GB)

2. **Verify Installation**
   - Open Minecraft Education Edition
   - Create test world to confirm it launches
   - Close Minecraft

### macOS

1. **Download from Apple App Store**
   - Search "Minecraft Education Edition"
   - Click **Get**
   - Authenticate with Apple ID

2. **Verify Installation**
   - Launch Minecraft
   - Create test world
   - Close Minecraft

---

## 🐍 Step 2: Install Python 3.10+

### Windows

1. **Download Python**
   - Visit [python.org](https://python.org)
   - Download **Python 3.11** or **3.12**
   - Run the installer

2. **Installation Steps**
   - ✅ Check "Add Python to PATH"
   - Select "Install Now"
   - Wait for completion

3. **Verify Installation**
   ```powershell
   python --version
   pip --version
   ```
   Should show: `Python 3.11.x` and `pip 23.x`

### macOS (using Homebrew)

1. **Install Homebrew** (if not already installed)
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python**
   ```bash
   brew install python@3.11
   ```

3. **Verify Installation**
   ```bash
   python3 --version
   pip3 --version
   ```

---

## 📦 Step 3: Install Node.js 18+

### Windows

1. **Download Node.js**
   - Visit [nodejs.org](https://nodejs.org)
   - Download **LTS version** (18.x or 20.x)
   - Run installer

2. **Installation Steps**
   - Accept license
   - Choose installation path
   - Enable "Add to PATH"
   - Click Install

3. **Verify Installation**
   ```powershell
   node --version
   npm --version
   ```

### macOS (using Homebrew)

```bash
brew install node@18
npm --version
```

---

## 🎨 Step 4: Install Visual Studio Code

### Windows & macOS

1. **Download VS Code**
   - Visit [code.visualstudio.com](https://code.visualstudio.com)
   - Download for your OS
   - Run installer

2. **Installation**
   - Follow setup wizard
   - Choose installation path
   - Complete installation

3. **Install Required Extensions**
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search and install:
     - **Python** (by Microsoft)
     - **GitHub Copilot** (by GitHub)
     - **Pylance** (by Microsoft)
     - **ESLint** (by Microsoft)

---

## ☁️ Step 5: Configure Microsoft Fabric Workspace

### Create Free Fabric Workspace

1. **Open Fabric**
   - Go to [fabric.microsoft.com](https://fabric.microsoft.com)
   - Sign in with Microsoft account
   - Click "Create" if no workspace exists

2. **Create Workspace**
   - Name: `Minecraft-RTI-Demo`
   - Capacity: Free trial or Premium capacity
   - Click Create

### Enable EventStream

1. **Navigate to Workspace**
   - Go to your new workspace
   - Click **+ New**
   - Search for **Eventstream**

2. **Create Eventstream**
   - Name: `minecraft-warehouse-events`
   - Create

3. **Get Connection Details**
   - Open Eventstream settings
   - Copy Event Hub connection string (save for later)
   - Note: Event Hub name

---

## 💾 Step 6: Clone Project Repository

### Using Git

1. **Open Terminal/PowerShell**

2. **Clone Repository**
   ```bash
   git clone https://github.com/microsoft/minecraft-rti-demo.git
   cd minecraft-rti-demo
   ```

3. **Verify Files**
   ```bash
   ls -la  # On Windows: dir
   ```
   Should show:
   - `fabric_bridge.py`
   - `warehouse_builder.py`
   - `warehouse_worker.py`
   - `MinecraftApp/` folder
   - `docs/` folder

### Alternative: Download ZIP

1. Go to GitHub repository
2. Click "Code" → "Download ZIP"
3. Extract to preferred location

---

## 🔧 Step 7: Install Python Dependencies

1. **Navigate to Project Directory**
   ```bash
   cd minecraft-rti-demo
   ```

2. **Create Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   
   # Activate it
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Requirements**
   ```bash
   pip install websockets azure-eventhub
   ```

4. **Verify Installation**
   ```bash
   python -c "import websockets; import azure.eventhub; print('OK')"
   ```

---

## 📚 Step 8: Install Fabric App Dependencies

1. **Navigate to Fabric App Directory**
   ```bash
   cd MinecraftApp
   ```

2. **Install Node Packages**
   ```bash
   npm install
   ```

3. **Verify Installation**
   ```bash
   npm list | head -20
   ```

---

## 🔐 Step 9: Configure Environment Variables

### Create `.env` File

1. **Create File**
   ```bash
   # In project root
   touch .env  # Windows: echo. > .env
   ```

2. **Add Configuration**
   ```env
   # Azure EventHub Connection
   EVENTHUB_CONNECTION_STRING=Endpoint=sb://...
   EVENTHUB_NAME=minecraft-warehouse-events
   
   # Local WebSocket Server
   HOST=localhost
   PORT=3000
   
   # Fabric Configuration
   FABRIC_WORKSPACE_ID=your-workspace-id
   FABRIC_EVENTSTREAM_ID=your-eventstream-id
   ```

3. **Get Your IDs**
   - Workspace ID: From Fabric URL bar
   - EventStream ID: From EventStream properties
   - Connection String: From Azure Portal

### Update fabric_bridge.py

1. **Open `fabric_bridge.py`**
   ```python
   # Update these lines:
   FABRIC_EVENT_STREAM_CONNECTION_STRING = os.getenv('EVENTHUB_CONNECTION_STRING')
   EVENT_HUB_NAME = os.getenv('EVENTHUB_NAME')
   ```

---

## ✅ Verification Checklist

Run through this to confirm everything is ready:

### Software Installed
```bash
minecraft-education --version  # Verify Minecraft installed
python --version               # Should be 3.10+
npm --version                  # Should be 8+
node --version                 # Should be 18+
```

### Fabric Setup
- [ ] Fabric workspace created and named
- [ ] EventStream created
- [ ] EventHub connection string obtained
- [ ] Workspace ID noted

### Local Environment
- [ ] Project cloned/downloaded
- [ ] Python virtual environment created
- [ ] Dependencies installed (`websockets`, `azure-eventhub`)
- [ ] Node packages installed (`npm install`)
- [ ] `.env` file created and populated

### Connectivity
- [ ] Minecraft launches without errors
- [ ] VS Code opens without issues
- [ ] GitHub Copilot chat available in VS Code
- [ ] Fabric workspace accessible

---

## 🚨 Troubleshooting Installation

### "Python not found" Error
```bash
# Verify Python installed
python --version

# If not found:
# 1. Add to PATH (Windows):
#    - System Properties > Environment Variables
#    - Add C:\Users\[YourName]\AppData\Local\Programs\Python\Python311
#
# 2. Or reinstall with "Add Python to PATH" checked
```

### "npm command not found"
```bash
# Reinstall Node.js
# Ensure "Add to PATH" is checked during installation

# Or verify installation:
where npm  # Windows
which npm  # macOS/Linux
```

### "Module not found: websockets"
```bash
# Reinstall in virtual environment
pip install --upgrade pip
pip install websockets azure-eventhub

# Verify:
python -c "import websockets"
```

### "Minecraft Edition Edition won't start"
- Ensure Windows/macOS is updated
- Check system meets minimum requirements
- Restart computer
- Reinstall Minecraft

### "Can't connect to Fabric workspace"
- Verify Fabric workspace created
- Sign in with correct Microsoft account
- Check internet connectivity
- Try incognito/private browser window

---

## 📦 Directory Structure After Setup

```
minecraft-rti-demo/
├── venv/                          # Python virtual environment
├── MinecraftApp/                  # React Fabric App
│   ├── src/
│   ├── package.json
│   └── ...
├── fabric_bridge.py               # WebSocket → EventHub bridge
├── warehouse_builder.py           # Minecraft warehouse builder
├── warehouse_worker.py            # Warehouse worker agent
├── .env                           # Configuration (created)
├── docs/                          # Documentation
├── prompts/                       # Copilot prompts
└── README.md
```

---

## 🎯 Next Steps

✅ **Installation complete!** Now proceed to:

1. **[Step 2: Build Minecraft Warehouse](./02-MINECRAFT-WAREHOUSE.md)**
   - Create warehouse structure
   - Set up zones and sections
   - Prepare for agent simulation

2. **[Step 3: Configure EventStream](./03-EVENTSTREAM-SETUP.md)**
   - Connect WebSocket bridge
   - Configure event parsing
   - Verify data flow

---

## 💡 Pro Tips

✅ **Keep terminal open**: Leave `fabric_bridge.py` running while testing

✅ **Use virtual environments**: Keep dependencies isolated

✅ **Save credentials**: Keep `.env` file secure (add to `.gitignore`)

✅ **Test incrementally**: Verify each component before moving forward

✅ **Monitor costs**: EventHub usage has Azure charges (typically <$1 for demo)

---

## 📞 Need Help?

- **Issues?** See [TROUBLESHOOTING.md](./TROUBLESHOOTING.md)
- **Questions?** Check [FAQ.md](./FAQ.md)
- **Still stuck?** See [Common Issues & Solutions](./TROUBLESHOOTING.md#installation-issues)

---

**Ready?** Proceed to [Step 2: Build Minecraft Warehouse →](./02-MINECRAFT-WAREHOUSE.md)
