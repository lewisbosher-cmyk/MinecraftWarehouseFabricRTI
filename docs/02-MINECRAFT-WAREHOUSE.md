# 2️⃣ Building the Minecraft Warehouse

Step-by-step guide to creating your warehouse environment in Minecraft Education Edition.

## 🎮 Overview

The warehouse is a sophisticated structure built in Minecraft that serves as your data simulation environment. It includes:
- **6 distinct zones** with color-coded sections
- **Automatic event tracking** by location
- **Realistic warehouse layout** for immersive data simulation
- **Section mapping** for accurate geolocation data

---

## 🚀 Quick Start (5 minutes)

### The Fast Way: Use Provided Builder

1. **Open Minecraft Education Edition**
   - Create new Flat World
   - Name: "Warehouse RTI Demo"

2. **Open Code Builder**
   - Press 'C' in-game

3. **Create New Python Project**
   - Click "New Project"
   - Name: "warehouse_builder"

4. **Copy Code**
   - Open [warehouse_builder.py](../scripts/warehouse_builder.py) in VS Code
   - Copy entire contents

5. **Paste and Run**
   - In Code Builder Python editor, paste code
   - Click Run (or press Play button)
   - Wait 3-4 minutes for building to complete

6. **Explore**
   - Exit Code Builder
   - Fly around to see the warehouse structure
   - Zones are color-coded

---

## 📐 Warehouse Design Specification

### Dimensions

```
Total Warehouse: 72 × 8 × 48 blocks
Coordinate Origin: X=100, Y=4, Z=100
```

### Zone Layout

```
                    FRONT (North)
                           
    LOADING BAY         STORAGE A      STORAGE B
    (Yellow Entry)    (Green Center)  (Lime Storage)
    
    PACKING STATION   STORAGE A      STORAGE B      CONTROL
    (Orange)          (Green Center)  (Lime Storage)  OFFICE
                                                       (Purple)
    FORBIDDEN ZONE    STORAGE A      STORAGE B
    (Red Restricted)  (Green Center)  (Lime Storage)
    
                    BACK (South)
```

### Zone Coordinates

| Zone | minX | maxX | minY | maxY | minZ | maxZ | Color | Purpose |
|------|------|------|------|------|------|------|-------|---------|
| Loading_Bay | 102 | 118 | 4 | 12 | 102 | 116 | Yellow | Incoming shipments |
| Storage_Area_A | 122 | 158 | 4 | 12 | 102 | 128 | Green | General inventory |
| Storage_Area_B | 122 | 158 | 4 | 12 | 130 | 144 | Lime | Fragile items |
| Packing_Station | 102 | 118 | 4 | 12 | 118 | 128 | Orange | Order fulfillment |
| Forbidden_Zone | 102 | 118 | 4 | 12 | 130 | 144 | Red | Restricted area |
| Control_Office | 160 | 170 | 4 | 12 | 102 | 114 | Purple | Command center |

---

## 🔨 Building Steps (Detailed)

### Step 1: Create World

1. **Launch Minecraft Education Edition**
2. **Click "Create"**
3. **Select "Create New"**
4. **World Settings**
   ```
   Name: Warehouse RTI Demo
   Game Mode: Survival or Creative (either works)
   World Type: Flat (recommended)
   Generate Structures: OFF
   Bonus Chest: OFF
   ```
5. **Click Create**
6. Wait for world to load

### Step 2: Enter Code Builder

1. **Press 'C'** to open Code Builder
2. **Create New Project**
   - Name: "warehouse_builder"
   - Language: Python
3. **Wait for editor** to open

### Step 3: Copy Builder Code

1. **In VS Code**, open [warehouse_builder.py](../scripts/warehouse_builder.py)
2. **Select All** (Ctrl+A)
3. **Copy** (Ctrl+C)
4. **In Code Builder editor**, click in code area
5. **Select All** and Delete existing template
6. **Paste** your code (Ctrl+V)

### Step 4: Run Builder

1. **Click "Run"** or press Play button
2. **Watch the magic happen!**
   - Takes 3-4 minutes to build
   - You'll see sections being filled with colored concrete
   - Ground floor appears first, then ceiling

3. **Wait for completion**
   - Check Minecraft window periodically
   - Code Builder shows progress
   - Building is done when Code Builder shows "Complete"

### Step 5: Exit and Explore

1. **Close Code Builder** (ESC or click X)
2. **Fly around the warehouse** (Press Space twice to fly in Creative/Adventure)
3. **Walk through each zone** to verify structure
4. **Test positions**
   - Stand in different zones
   - Note position changes (F3 shows coordinates in Java, press coordinates button in Education)

---

## 🎨 Warehouse Features

### Structural Elements

**Floors & Ceilings**
- Floor: Gray concrete (easy to see in video)
- Ceiling: Light gray concrete
- Clear distinction between ground and overhead

**Walls**
- Black concrete perimeter
- Helps define warehouse boundaries

**Entry Point**
- Double-height opening on west wall
- Sea lantern (glowing) accent lighting

**Interior Lighting**
- Sea lantern strips run east-west
- Three rows providing even illumination
- Makes warehouse visible in recordings

**Color Zones**
- Each zone has distinct color
- Easy visual identification
- Helps with navigation and videos

### Design Benefits

✅ **Large enough** for realistic agent movement
✅ **Small enough** for complete simulation in 5-10 minutes
✅ **Color-coded** for easy identification
✅ **Well-lit** for screen recording
✅ **Pre-measured** for exact event tracking
✅ **Expandable** - add more zones as needed

---

## 📍 Working with Coordinates

### Getting Your Position

1. **In Minecraft**
   - Look at bottom-left corner
   - Shows your XYZ coordinates
   - Note: Y is height, XZ is horizontal

2. **Understanding Coordinates**
   ```
   X = East-West (increases going East)
   Y = Up-Down (increases going Up)
   Z = North-South (increases going South)
   ```

### Finding Zone Boundaries

Example: To find if you're in Storage_Area_A:
```
If your position is:
X=130, Y=6, Z=110

Check against zone specs:
Storage_Area_A: X 122-158, Y 4-12, Z 102-128

- Is 130 between 122 and 158? ✅ Yes (X OK)
- Is 6 between 4 and 12? ✅ Yes (Y OK)  
- Is 110 between 102 and 128? ✅ Yes (Z OK)

You're in Storage_Area_A! ✅
```

---

## 🧪 Verification Checklist

After building, verify these elements:

### Visual Inspection

- [ ] **Floor** is uniform gray concrete
- [ ] **Ceiling** is light gray concrete
- [ ] **Walls** are solid black concrete
- [ ] **Each zone** has distinct color (see Zone Layout)
- [ ] **Lighting** illuminates all areas
- [ ] **Entry point** is clearly visible
- [ ] **No floating blocks** or gaps in structure

### Functionality Check

1. **Test Zone Detection**
   - Fly to each zone
   - Check position in each color area
   - Note coordinates match zone specs

2. **Test Movement**
   - Walk from one zone to another
   - Movement should be smooth
   - No collision issues

3. **Visibility**
   - Can you see all zones from above?
   - Is lighting adequate for recording?
   - Any shadow issues?

---

## 🎬 Recording Preparation

### Camera Positions

Use these positions for good warehouse views:

**Overhead View**
```
Position: X=130, Y=20, Z=120
Direction: Looking down
Purpose: See all zones at once
```

**Perspective View**
```
Position: X=110, Y=8, Z=110
Direction: Looking around
Purpose: See agent movement in detail
```

**Tracking View**
```
Position: X=135, Y=12, Z=120
Direction: Follow agent from side
Purpose: Monitor specific zone activity
```

### Setting a Spawn Point

1. **Build a command block** at your preferred default location
2. Or use `/spawnpoint` command
3. Recommended spawn: X=100, Y=13, Z=100 (above warehouse)

---

## 🛠️ Customization

### Adding More Zones

1. **Define new zone in code:**
   ```python
   {"name": "NewZone", "minX": 160, "maxX": 180, "minY": 4, "maxY": 12, "minZ": 102, "maxZ": 116}
   ```

2. **Add color in builder:**
   ```python
   blocks.fill(BLUE_CONCRETE, rel(60, 0, 2), rel(80, 0, 16), FillOperation.REPLACE)
   ```

3. **Update warehouse_worker.py** to track new zone

### Changing Materials

1. **Floor color:**
   ```python
   blocks.fill(WHITE_CONCRETE, rel(0, 0, 0), rel(72, 0, 48), FillOperation.REPLACE)
   ```

2. **Zone color:**
   ```python
   blocks.fill(BLUE_CONCRETE, ...)  # Change from GREEN_CONCRETE
   ```

Available colors:
- WHITE_CONCRETE
- BLACK_CONCRETE
- GRAY_CONCRETE
- RED_CONCRETE
- ORANGE_CONCRETE
- YELLOW_CONCRETE
- GREEN_CONCRETE
- LIME_CONCRETE
- CYAN_CONCRETE
- BLUE_CONCRETE
- PURPLE_CONCRETE
- PINK_CONCRETE

### Adjusting Size

1. **Find these variables:**
   ```python
   ORIGIN_X = 100
   ORIGIN_Y = 4
   ORIGIN_Z = 100
   ```

2. **Modify zone dimensions:**
   ```python
   {"name": "Zone", "minX": 102, "maxX": 150, ...}  # Wider zone
   ```

3. **Test new coordinates** match fabric_bridge.py

---

## 🐛 Troubleshooting

### "Code won't paste into Code Builder"

**Solution:**
1. Open Code Builder text editor
2. Press Ctrl+A to select all
3. Press Delete to clear template
4. Then paste your code

### "Building takes forever or crashes"

**Solution:**
1. Try smaller zones initially
2. Run builder in empty world
3. Reduce block count if needed
4. Check Minecraft available memory

### "Can't see the warehouse"

**Solution:**
1. Fly higher to see full structure
2. Press F5 to get better perspective
3. Move to coordinates: X=130, Y=20, Z=120
4. Look down (press C then adjust view)

### "Zones appear in wrong colors"

**Solution:**
1. Verify block type names in code
2. Ensure each FILL command has correct zone
3. Compare coordinates with zone table
4. Rebuild if colors are critical to demo

---

## 📊 Data Integration

### Coordinate Mapping in Events

When agent moves, events include location:

```python
# In warehouse_worker.py, events use these zones:
"location": section_for_position(x, y, z)
```

The section_for_position function:
```python
def section_for_position(x, y, z):
    for zone in zones:
        if is_in_zone(x, y, z, zone):
            return zone["name"]
    return "Outside_Warehouse"
```

### Verifying Zone Detection

1. **Place agent in zone**
2. **Check position in Minecraft**
3. **Verify event reports correct zone**
4. **Repeat for each zone**

---

## 🎯 Next Steps

✅ **Warehouse built!** Continue with:

1. **[Step 3: Configure EventStream](./03-EVENTSTREAM-SETUP.md)**
   - Start the WebSocket bridge
   - Connect Minecraft to Fabric
   - Verify event flow

2. **Or build the agent first:**
   - Use [warehouse_worker.py](../scripts/warehouse_worker.py)
   - Or generate with Copilot using [EXACT-REPLICATION-PROMPT.md](../prompts/EXACT-REPLICATION-PROMPT.md)

---

## 💡 Pro Tips

✅ **Record your build**: Use Windows Game Bar (Win+Alt+R) to record the warehouse creation

✅ **Save the world**: Back up your world after building (File > Export)

✅ **Test movement**: Try teleporting between zones with `/tp` command

✅ **Measure distances**: Use `/measure` command to verify zone sizes

✅ **Create copies**: Export world to share with team members

---

**Warehouse ready?** → [Next: Configure EventStream](./03-EVENTSTREAM-SETUP.md)
