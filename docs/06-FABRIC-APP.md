# 6️⃣ Building the Fabric App

Create an interactive real-time analytics dashboard using React and Fabric visuals.

## 🎨 Overview

The Fabric App is a React/TypeScript application that visualizes real-time warehouse data from your Semantic Model.

```
Semantic Model
      ↓
Rayfin (Data connection)
      ↓
React Components
      ↓
Visualizations (Datagrid, Charts, Cards)
      ↓
Real-time Dashboard
```

---

## 🚀 Quick Setup (10 minutes)

### Step 1: Project Structure

The Fabric App is in `MinecraftApp/` folder:

```
MinecraftApp/
├── src/
│   ├── App.tsx                    # Main component
│   ├── main.tsx                   # Entry point
│   ├── components/                # Reusable components
│   ├── hooks/                     # Custom hooks
│   ├── lib/                       # Utilities
│   └── services/                  # Business logic
├── package.json                   # Dependencies
├── tsconfig.json                  # TypeScript config
├── vite.config.ts                 # Build config
└── fabric.yaml                    # Fabric configuration
```

### Step 2: Install Dependencies

```bash
cd MinecraftApp
npm install
```

### Step 3: Configure Rayfin

1. **Check fabric.yaml**
   ```yaml
   workspaces:
     - workspace_id: "YOUR_WORKSPACE_ID"
       name: "Minecraft-RTI-Demo"
   ```

2. **Update IDs if needed:**
   - `workspace_id`: Your Fabric workspace ID
   - `semantic_model_id`: Your warehouse-analytics model ID

### Step 4: Start Development Server

```bash
npm run dev
```

Expected output:
```
Local:   http://localhost:5173/
Press 'q' to quit
```

### Step 5: Open in Browser

1. Navigate to http://localhost:5173
2. You should see the Fabric App loading
3. Authenticate with your Microsoft account if prompted

---

## 📊 Key Components

### Main Dashboard Component

**File:** `src/App.tsx`

```tsx
import React from 'react';
import { useSemanticModelQuery } from './hooks/use-semantic-model-query';

export const App: React.FC = () => {
  const { data, loading, error } = useSemanticModelQuery(
    `EVALUATE warehouse_activity`
  );

  if (loading) return <div>Loading warehouse data...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div className="warehouse-dashboard">
      <h1>Warehouse RTI Dashboard</h1>
      <MetricsCards data={data} />
      <ActivityTimeline data={data} />
      <ZoneActivity data={data} />
    </div>
  );
};
```

### Card Component (KPIs)

```tsx
const MetricsCards: React.FC<{data: WarehouseData[]}> = ({ data }) => (
  <div className="metrics-row">
    <Card title="Total Items" value={calculateTotal(data)} />
    <Card title="Avg Efficiency" value={calculateEfficiency(data)} />
    <Card title="Active Zones" value={getUniqueZones(data).length} />
    <Card title="Events" value={data.length} />
  </div>
);
```

### Datagrid Component

```tsx
const ActivityTimeline: React.FC<{data: WarehouseData[]}> = ({ data }) => (
  <DataGridTable
    data={data}
    columns={[
      { key: 'timestamp', name: 'Time' },
      { key: 'location', name: 'Zone' },
      { key: 'efficiency_score', name: 'Efficiency' },
      { key: 'items_processed', name: 'Items' }
    ]}
  />
);
```

---

## 🎯 Building Your Dashboard

### Step 1: Create Basic Layout

1. **Import components**
   ```tsx
   import { Card, DataGridTable, LineChart } from '@microsoft/fabric-visuals';
   ```

2. **Create layout structure**
   ```tsx
   <div className="dashboard-grid">
     <div className="kpi-row">
       <Card />
       <Card />
       <Card />
     </div>
     <div className="charts-row">
       <LineChart />
       <BarChart />
     </div>
     <div className="table-row">
       <DataGridTable />
     </div>
   </div>
   ```

### Step 2: Add KPI Cards

```tsx
<Card
  title="Total Items Processed"
  value={totalItems}
  subtitle="this shift"
  icon="📦"
/>

<Card
  title="Average Efficiency"
  value={`${avgEfficiency.toFixed(1)}%`}
  subtitle="warehouse-wide"
  icon="⚡"
/>

<Card
  title="Active Zones"
  value={activeZones}
  subtitle="currently in use"
  icon="🏭"
/>
```

### Step 3: Add Timeline Chart

```tsx
<LineChart
  title="Efficiency Timeline"
  data={efficiencyData}
  xKey="timestamp"
  yKey="efficiency_score"
  color="#00A4EF"
/>
```

### Step 4: Add Zone Breakdown

```tsx
<BarChart
  title="Items by Zone"
  data={zoneData}
  xKey="location"
  yKey="items_processed"
  color="#7FBA00"
/>
```

### Step 5: Add Live Data Table

```tsx
<DataGridTable
  title="Recent Activity"
  data={activityData}
  columns={[
    { key: 'timestamp', name: 'Time', width: 150 },
    { key: 'location', name: 'Zone', width: 150 },
    { key: 'items_processed', name: 'Items', width: 100 },
    { key: 'efficiency_score', name: 'Efficiency', width: 120 }
  ]}
  sortBy="timestamp"
  sortOrder="descending"
/>
```

---

## 🔄 Real-time Data Binding

### Hook: useSemanticModelQuery

```tsx
const { data, loading, error, refresh } = useSemanticModelQuery(query);

// Auto-refresh every 5 seconds
useEffect(() => {
  const interval = setInterval(refresh, 5000);
  return () => clearInterval(interval);
}, [refresh]);
```

### Hook: useWarehouseMetrics

```tsx
const { 
  totalItems, 
  avgEfficiency, 
  activeZones,
  timestamp 
} = useWarehouseMetrics(data);

// Returns calculated metrics
```

---

## 🎨 Styling

### Using Tailwind CSS

```tsx
<div className="p-6 bg-gradient-to-r from-blue-50 to-blue-100">
  <h1 className="text-3xl font-bold text-gray-800">
    Warehouse Analytics
  </h1>
</div>
```

### Microsoft Colors

```tsx
// Use Microsoft Fabric colors
const colors = {
  primary: '#00A4EF',      // Blue
  success: '#7FBA00',      // Green
  warning: '#FFB900',      // Amber
  error: '#F25022',        // Red
  background: '#FFFFFF',   // White
  text: '#505050'          // Dark gray
};
```

---

## 📦 Building for Production

### Step 1: Build Fabric App

```bash
npm run build
```

This creates optimized bundle in `dist/` folder.

### Step 2: Deploy to Fabric

1. **In Fabric, create App**
   - Go to workspace
   - Click "+ New"
   - Select "App"
   - Name: "warehouse-analytics-app"

2. **Upload built app**
   - Build complete with: `npm run build`
   - Upload `dist/` folder contents
   - Configure app settings

3. **Share App**
   - Go to app settings
   - Add users/groups
   - Set permissions (view/edit)

---

## 🔐 Authentication

The app uses Rayfin auth provider for Fabric:

```tsx
import { FabricAuthProvider } from '@microsoft/rayfin-auth-provider-fabric';

<FabricAuthProvider>
  <App />
</FabricAuthProvider>
```

---

## 🧪 Testing

### Unit Tests

```bash
npm run test
```

### Visual Testing

```bash
npm run preview
```

---

## 📊 Example Dashboard Layout

```
┌─────────────────────────────────────────────┐
│           WAREHOUSE RTI DASHBOARD            │
├─────────────────────────────────────────────┤
│  [Total Items: 145] [Efficiency: 82.5%]    │
│  [Active Zones: 5] [Duration: 15 min]       │
├─────────────────────────────────────────────┤
│                                             │
│  ┌────────────────┐  ┌────────────────┐   │
│  │  Efficiency    │  │  Items by      │   │
│  │  Timeline      │  │  Zone          │   │
│  │  (Line Chart)  │  │  (Bar Chart)   │   │
│  └────────────────┘  └────────────────┘   │
│                                             │
├─────────────────────────────────────────────┤
│  Recent Activity                            │
│  ┌──────────┬─────────┬────────┬──────┐   │
│  │ Time     │ Zone    │ Items  │ Eff% │   │
│  ├──────────┼─────────┼────────┼──────┤   │
│  │ 10:30:45 │ Storage │ 8      │ 85   │   │
│  │ 10:30:40 │ Loading │ 5      │ 80   │   │
│  └──────────┴─────────┴────────┴──────┘   │
└─────────────────────────────────────────────┘
```

---

## 🐛 Troubleshooting

### "App won't connect to semantic model"

**Solutions:**
1. Verify workspace ID in fabric.yaml
2. Verify semantic model ID correct
3. Check authentication (sign in with Fabric account)
4. Verify semantic model has data

### "Charts show no data"

**Check:**
1. Query syntax correct
2. Column names match semantic model
3. Data exists in model (test with KQL)
4. Refresh page (F5)

### "Styling looks broken"

**Solutions:**
1. Clear browser cache (Ctrl+Shift+Delete)
2. Restart dev server (npm run dev)
3. Check Tailwind classes loaded
4. Verify CSS build complete

---

## 📈 Performance Optimization

### Lazy Load Data

```tsx
const [showTable, setShowTable] = React.useState(false);

// Only load table data when needed
{showTable && <ActivityTable data={data} />}
```

### Cache Results

```tsx
const cachedData = React.useMemo(() => processData(data), [data]);
```

### Debounce Updates

```tsx
const [searchTerm, setSearchTerm] = React.useState('');
const debouncedSearch = useDebounce(searchTerm, 300);
```

---

## 📚 Next Steps

✅ **Fabric App created!** Continue with:

1. **Customize dashboard** with your metrics
2. **Add more visualizations** as needed
3. **Deploy to Fabric** for team sharing
4. **Monitor performance** in production

---

## 💡 Pro Tips

✅ **Start simple**: Build minimal viable dashboard first

✅ **Use TypeScript**: Catches errors before runtime

✅ **Test locally**: Always test in dev before deploying

✅ **Monitor data**: Use browser DevTools to check data flow

✅ **Get feedback**: Share dashboard and iterate

---

**App built?** → [Complete! You now have end-to-end RTI pipeline]

Next: Explore advanced customizations in [TECHNICAL-REFERENCE.md](./TECHNICAL-REFERENCE.md)
