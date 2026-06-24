# 4️⃣ Eventhouse & KQL Data Pipeline

Set up your data warehouse and create queries for real-time analytics.

## 📊 Overview

Eventhouse is Fabric's real-time analytics database built on KQL (Kusto Query Language). Your events flow from EventStream → Eventhouse → Semantic Model → Fabric App.

```
EventStream                Eventhouse               Semantic Model
    ↓                          ↓                         ↓
warehouse_events     raw_warehouse_events      processed_metrics
  (JSON)            (Parsed, structured)        (Business logic)
```

### Step 1: Add Eventhouse Destination in Eventstream

1. Open your Eventstream (`minecraft-warehouse-events`)
2. Click `+ Add destination`
3. Select `Eventhouse`
4. Fill destination details:
   - Workspace
   - Eventhouse item
   - Database name
   - Table name (raw table)
5. Save destination

When destination details are complete, Eventstream automatically creates and ingests into the raw KQL table. No manual column mapping is required for the initial raw ingestion table.

### Step 2: Run Data Through the Pipeline

1. Start `fabric_bridge.py`
2. In Minecraft run:
   - `/connect localhost:3000`
   - `run_shift`
3. Wait 15-60 seconds for ingestion visibility

---

## 📋 Validate Auto-Created Raw KQL Table

### Check available tables

```kql
.show tables
```

Find the table name you configured in destination.

### Preview raw records

```kql
<raw_table_name>
| take 100
```

### Verify recent ingestion

```kql
<raw_table_name>
| summarize rows = count() by bin(ingestion_time(), 1m)
| order by ingestion_time_ desc
```

---

## 🔍 Essential KQL Queries (Raw Table)

Use your destination table name in place of `<raw_table_name>`.

### Query 1: Latest events

```kql
<raw_table_name>
| order by ingestion_time() desc
| take 100
```

### Query 2: Event count by location

If your payload fields are extracted as columns:

```kql
<raw_table_name>
| summarize events = count() by location
| order by events desc
```

If your raw table stores payload as dynamic/json column, adapt with `parse_json()` based on your schema.

### Query 3: Activity over time

```kql
<raw_table_name>
| summarize events = count() by bin(ingestion_time(), 1m)
| render timechart
```

---

## 📈 Optional: Create a Curated Table/View

After raw ingestion is stable, create a curated projection for analytics-friendly columns.

```kql
.create-or-alter function warehouse_curated() {
    <raw_table_name>
    | project ingestion_ts = ingestion_time(), *
}
```

Or create a materialized view once your finalized column strategy is clear.

---

## 🔄 Data Pipeline Notes

- Source auth/transport: Eventstream Custom Endpoint (Event Hub protocol, SAS key)
- Sink: Eventstream Destination -> Eventhouse
- Raw table creation: automatic from destination configuration
- Manual column configuration: not required for initial raw table creation

---

## 🎯 Testing Your Setup

### Test 1: Destination healthy

In Eventstream canvas, verify destination node shows healthy/running status.

### Test 2: Raw table receives rows

```kql
<raw_table_name>
| count
```

Expected: count increases after running `run_shift`.

### Test 3: Recent events present

```kql
<raw_table_name>
| where ingestion_time() > now(-10m)
| take 20
```

---

## 🐛 Troubleshooting

### Destination created but table missing

1. Re-open destination settings and confirm Eventhouse/database/table names
2. Save destination again
3. Send new test events and wait 1-2 minutes
4. Run `.show tables` again

### Table exists but no rows

1. Confirm Eventstream source preview shows incoming events
2. Confirm destination status is healthy
3. Confirm `fabric_bridge.py` is running with valid credentials
4. Trigger events with `run_shift`

### Raw payload not in expected columns

1. This is normal for raw ingestion depending on destination mode
2. Query raw shape first (`take 5`)
3. Build a curated function/view for semantic model use

---

## 🎯 Next Steps

1. Use raw table as source for curated KQL layer
2. Build semantic model on curated dataset
3. Wire visuals in Fabric App

Next: [Step 5: Create Semantic Model](./05-SEMANTIC-MODEL.md)
