# 5️⃣ Semantic Model

Create the business intelligence layer between Eventhouse and your Fabric App.

## 📐 Overview

The Semantic Model transforms raw warehouse data into business metrics:

```
Eventhouse Tables       Semantic Model          Fabric App
(Raw data)              (Business logic)        (Dashboard)
    ↓                       ↓                       ↓
warehouse_events  →   warehouse_activity  →  Real-time Dashboard
zone_capacity     →   capacity_metrics    →  Zone Status
                      efficiency_trends   →  Performance Charts
```

---

## 🚀 Quick Setup (5 minutes)

### Step 1: Create Semantic Model

1. **Go to Fabric workspace**
   - [fabric.microsoft.com](https://fabric.microsoft.com)
   - Select your workspace

2. **Create Semantic Model**
   - Click "+ New"
   - Search "Semantic Model"
   - Click "Semantic Model"
   - Name: `warehouse-analytics`
   - Create

3. **Wait for provisioning** (~1-2 minutes)

### Step 2: Connect Eventhouse

1. **In Semantic Model**, click "+" to add data
2. **Select "Eventhouse"**
3. **Choose connection**
   - Select your Eventhouse
   - Select `warehouse_events` table
   - Click Load

4. **Configure columns**
   - Verify all columns loaded
   - Check data types correct

---

## 📊 Create Tables & Measures

### Table: WarehouseActivity

1. **Base table from `warehouse_events`**
   - All warehouse_activity events
   - Columns:
     - `timestamp` (datetime)
     - `location` (text)
     - `items_processed` (whole number)
     - `zone_transitions` (whole number)
     - `efficiency_score` (decimal)
     - `action` (text)

2. **Add calculated columns:**

```DAX
Zone Efficiency Level = 
SWITCH(TRUE(),
    [efficiency_score] >= 90, "Excellent",
    [efficiency_score] >= 75, "Good",
    [efficiency_score] >= 60, "Fair",
    "Needs Improvement")

Time Period = 
FORMAT([timestamp], "HH:00")
```

### Table: ZoneCapacityAlerts

1. **Add second table from `warehouse_events`**
   - Filter where `event_type = "zone_capacity_alert"`
   - Columns:
     - `timestamp` (datetime)
     - `location` (text)
     - `zone_utilization` (decimal)

---

## 📈 Create Key Measures

### Total Items Processed
```DAX
Total Items = SUM(WarehouseActivity[items_processed])
```

### Average Efficiency
```DAX
Avg Efficiency = AVERAGE(WarehouseActivity[efficiency_score])
```

### Events Count
```DAX
Event Count = COUNTA(WarehouseActivity[timestamp])
```

### Shift Duration (minutes)
```DAX
Shift Duration = DIVIDE(
    [Event Count] * 5,  // 5 seconds per event
    60,                  // Convert to minutes
    0)
```

### Zone Utilization Risk
```DAX
High Utilization = 
CALCULATE(
    COUNTA(ZoneCapacityAlerts[timestamp]),
    ZoneCapacityAlerts[zone_utilization] >= 80)
```

### Efficiency Trend
```DAX
Efficiency Trend = 
VAR CurrentPeriod = 
    CALCULATE([Avg Efficiency], 
        DATESBETWEEN(WarehouseActivity[timestamp], TODAY()-1, TODAY()))
VAR PreviousPeriod = 
    CALCULATE([Avg Efficiency], 
        DATESBETWEEN(WarehouseActivity[timestamp], TODAY()-2, TODAY()-1))
RETURN DIVIDE(CurrentPeriod - PreviousPeriod, PreviousPeriod, 0)
```

---

## 🔗 Create Relationships

### Location Dimension

1. **Create Location table** (optional but recommended)
   ```DAX
   {
       "Zone": ["Loading_Bay", "Storage_Area_A", "Storage_Area_B", "Packing_Station", "Forbidden_Zone", "Control_Office"],
       "Zone_Type": ["Inbound", "Storage", "Storage", "Outbound", "Restricted", "Admin"],
       "Capacity": [50, 100, 80, 60, 30, 20]
   }
   ```

2. **Link to WarehouseActivity**
   - Relationship: `WarehouseActivity[location]` → `Location[Zone]`
   - Cardinality: Many-to-One
   - Direction: Single

---

## 📋 Create Hierarchies

### Zone Hierarchy
```
Location
├── Zone_Type
│   ├── Storage
│   │   ├── Storage_Area_A
│   │   └── Storage_Area_B
│   ├── Inbound
│   │   └── Loading_Bay
│   └── Outbound
│       └── Packing_Station
```

---

## 🎯 Performance Optimization

### Row-Level Security (RLS)

Restrict data by zone:

```DAX
[location] = USERNAME()  // If user name matches zone name
```

### Aggregations

Create pre-aggregated tables for faster queries:

```DAX
Hourly Summary = 
SUMMARIZE(
    WarehouseActivity,
    WarehouseActivity[location],
    ROUNDDOWN(WarehouseActivity[timestamp], 1/24),
    "Items": SUM(WarehouseActivity[items_processed]),
    "Avg_Efficiency": AVERAGE(WarehouseActivity[efficiency_score]),
    "Event_Count": COUNTA(WarehouseActivity[timestamp]))
```

---

## 🔄 Refresh Schedule

### Set up incremental refresh

1. **In Semantic Model settings**
   - Go to Refresh settings
   - Enable incremental refresh

2. **Configure retention**
   ```
   Keep data for last: 30 days
   Incrementally refresh data for last: 2 days
   ```

3. **Schedule refresh**
   ```
   Frequency: Every hour
   Time: Any time
   ```

---

## 📊 Data Lineage

Document how data transforms:

```
Source: warehouse_events (Eventhouse)
    ↓
[Filter] where event_type = "warehouse_activity"
    ↓
[Transform] Add calculated columns
    - Zone Efficiency Level
    - Time Period
    ↓
[Aggregate] By zone and time
    ↓
[Measure] KPI calculations
    - Total Items
    - Avg Efficiency
    - Event Count
    ↓
[Consume] In Fabric App
```

---

## ✅ Testing Your Model

### Test 1: Data Connection

```DAX
// In query editor, test connection
= Eventhouse.Contents("minecraft-warehouse-analytics")
```

Expected: Connection successful, can see tables

### Test 2: Measure Calculation

1. **Create measure:**
   ```DAX
   Test Measure = COUNTA(WarehouseActivity[timestamp])
   ```

2. **Pin to dashboard**
3. **Verify value > 0**

### Test 3: Build Simple Report

1. **Create visual:** Card showing `[Total Items]`
2. **Create visual:** Table showing Location and `[Avg Efficiency]`
3. **Verify data appears**

---

## 🎓 Key Concepts

### Fact vs. Dimension Tables

| Type | Purpose | Example |
|------|---------|---------|
| **Fact** | Measures & metrics | WarehouseActivity |
| **Dimension** | Attributes | Location, Time |

### Measures vs. Calculated Columns

| Type | Purpose | Scope |
|------|---------|-------|
| **Measure** | Aggregate calculations | Entire table context |
| **Calc Column** | Row-level values | Single row |

---

## 🔐 Security

### Restrict Data Access

```DAX
// In semantic model security rules
[location] = USERPRINCIPALNAME()
```

### Audit & Monitoring

- Enable query auditing in Fabric workspace
- Monitor who accesses warehouse data
- Track model performance

---

## 📈 Advanced Patterns

### Year-over-Year Comparison

```DAX
YoY Comparison = 
VAR CurrentYear = 
    CALCULATE([Total Items], 
        YEAR(WarehouseActivity[timestamp]) = YEAR(TODAY()))
VAR PreviousYear = 
    CALCULATE([Total Items], 
        YEAR(WarehouseActivity[timestamp]) = YEAR(TODAY()) - 1)
RETURN DIVIDE(CurrentYear - PreviousYear, PreviousYear, 0)
```

### Rolling Averages

```DAX
Rolling Avg Efficiency 7D = 
CALCULATE(
    [Avg Efficiency],
    DATESINPERIOD(WarehouseActivity[timestamp], MAX(WarehouseActivity[timestamp]), -7, DAY))
```

---

## 🐛 Troubleshooting

### "No data in model"

**Solutions:**
1. Verify Eventhouse connection active
2. Check table and column names
3. Verify Eventhouse has data:
   ```kql
   warehouse_events | count
   ```
4. Refresh model manually

### "Measures show 0 or blank"

**Check:**
1. Correct table selected
2. Column exists in table
3. Data types match (e.g., numbers not text)
4. Filter context is correct

### "Query performance slow"

**Optimize:**
1. Add relationships between tables
2. Create aggregations
3. Use column-based filtering
4. Reduce data volume with filters

---

## 📚 Next Steps

✅ **Semantic Model created!** Continue with:

1. **[Step 6: Build Fabric App](./06-FABRIC-APP.md)**
   - Create real-time dashboard
   - Add interactive visualizations
   - Deploy to production

2. **Or explore your model:**
   - Test measures
   - Create reports
   - Understand data relationships

---

## 💡 Pro Tips

✅ **Start simple**: Create 2-3 key measures first, expand later

✅ **Name consistently**: Use clear, descriptive measure names

✅ **Document measures**: Add descriptions to every measure

✅ **Monitor refresh**: Check refresh history in workspace

✅ **Version control**: Document model changes in Git

---

**Model complete?** → [Next: Build Fabric App](./06-FABRIC-APP.md)
