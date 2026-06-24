# 🎨 Custom Agent Prompt Template for GitHub Copilot

Use this template to create your own custom Minecraft agent scenarios. Adapt the prompt to define any data-generating behavior you want.

## 📌 How to Use This Template

1. Copy the template below
2. Replace the bracketed sections `[YOUR_SCENARIO]` with your details
3. Paste into **GitHub Copilot Chat** (VS Code)
4. Copilot will generate the complete Python agent code
5. Integrate with the rest of the pipeline

---

## 🔧 Template Prompt

```
I'm building a Minecraft education project that simulates [YOUR_SCENARIO].

The Minecraft warehouse has these zones:
- Zone A: [DESCRIPTION]
- Zone B: [DESCRIPTION]  
- Zone C: [DESCRIPTION]

I need a Python Code Builder script (for Minecraft Education Edition) 
that will:

1. [BEHAVIOR 1] - [Description of what should happen]
2. [BEHAVIOR 2] - [Description of what should happen]
3. [BEHAVIOR 3] - [Description of what should happen]

Each action should be triggered by the command: [COMMAND_NAME]

The agent should track and report:
- [METRIC 1]: [What to measure]
- [METRIC 2]: [What to measure]
- [METRIC 3]: [What to measure]

Every [TIME_INTERVAL], send events via chat with prefix "FABRIC_EVENT|" 
in this JSON format:
{
  "event_type": "[EVENT_TYPE]",
  "agent_name": "[AGENT_NAME]",
  "location": "[LOCATION]",
  "timestamp": "[ISO_TIMESTAMP]",
  "metric_1": [VALUE],
  "metric_2": [VALUE],
  "details": "[ADDITIONAL_DETAILS]"
}

Please generate the complete Python script for Minecraft Code Builder.
Include error handling and the ability to stop with the "stop_shift" command.
```

---

## 📋 Pre-Built Scenarios (Copy & Paste Ready)

### Scenario 1: Warehouse Inventory Management
```
I'm building a Minecraft warehouse inventory management system.

The warehouse has these zones:
- Loading Bay: Incoming shipments area
- Storage Area A: General inventory storage
- Storage Area B: Fragile items storage
- Packing Station: Order fulfillment area

I need a Python Code Builder script that will:

1. Track inventory movements between zones
2. Simulate picking items for orders
3. Generate alerts when zones reach capacity

Each action should be triggered by the command: "run_shift"

The agent should track and report:
- items_moved: Number of items moved between zones
- zone_utilization: Current capacity percentage per zone
- orders_fulfilled: Number of orders completed

Every 5 seconds, send events via chat with prefix "FABRIC_EVENT|" in this JSON format:
{
  "event_type": "inventory_movement",
  "agent_name": "warehouse_worker",
  "location": "storage_area_a",
  "timestamp": "2024-01-15T10:30:45Z",
  "items_moved": 5,
  "zone_utilization": 75,
  "details": "Picked 5 items for order #12345"
}

Please generate the complete Python script for Minecraft Code Builder.
Include error handling and the ability to stop with the "stop_shift" command.
```

### Scenario 2: Manufacturing Production Line
```
I'm building a Minecraft manufacturing production line simulator.

The production line has these zones:
- Assembly Station 1: Component assembly
- Assembly Station 2: Sub-assembly
- Quality Control: Testing and validation
- Packaging Station: Final packaging

I need a Python Code Builder script that will:

1. Simulate moving items through production stages
2. Track quality metrics and reject rates
3. Generate production reports

Each action should be triggered by the command: "start_production"

The agent should track and report:
- units_produced: Number of units completed
- defect_rate: Percentage of defective units
- cycle_time: Average time per unit

Every 10 seconds, send events via chat with prefix "FABRIC_EVENT|" in this JSON format:
{
  "event_type": "production_event",
  "agent_name": "production_manager",
  "location": "assembly_station_1",
  "timestamp": "2024-01-15T10:30:45Z",
  "units_produced": 12,
  "defect_rate": 2.5,
  "cycle_time": 45,
  "details": "Completed batch #567"
}

Please generate the complete Python script for Minecraft Code Builder.
Include error handling and the ability to stop with the "stop_production" command.
```

### Scenario 3: Retail Store Operations
```
I'm building a Minecraft retail store operations simulator.

The store has these zones:
- Stockroom: Inventory storage
- Shelf Area A: Main sales floor
- Shelf Area B: Premium products
- Checkout Counter: Point of sale

I need a Python Code Builder script that will:

1. Simulate restocking shelves from stockroom
2. Track customer movements and sales
3. Generate real-time store metrics

Each action should be triggered by the command: "open_store"

The agent should track and report:
- items_stocked: Items moved to shelves
- transactions: Number of sales
- shelf_occupancy: Percentage of shelf space used

Every 8 seconds, send events via chat with prefix "FABRIC_EVENT|" in this JSON format:
{
  "event_type": "store_event",
  "agent_name": "store_manager",
  "location": "shelf_area_a",
  "timestamp": "2024-01-15T10:30:45Z",
  "items_stocked": 8,
  "transactions": 3,
  "shelf_occupancy": 85,
  "details": "Restocked electronics section"
}

Please generate the complete Python script for Minecraft Code Builder.
Include error handling and the ability to stop with the "close_store" command.
```

### Scenario 4: Logistics & Delivery Network
```
I'm building a Minecraft logistics delivery network simulator.

The network has these zones:
- Distribution Center: Main hub
- Regional Hub A: Eastern region
- Regional Hub B: Western region
- Local Pickup Point: Customer collection area

I need a Python Code Builder script that will:

1. Simulate moving packages between hubs
2. Track delivery times and route efficiency
3. Generate logistics metrics

Each action should be triggered by the command: "start_deliveries"

The agent should track and report:
- packages_processed: Packages moved through system
- average_delivery_time: Time per delivery
- route_efficiency: Percentage of optimal routing

Every 6 seconds, send events via chat with prefix "FABRIC_EVENT|" in this JSON format:
{
  "event_type": "delivery_event",
  "agent_name": "logistics_coordinator",
  "location": "distribution_center",
  "timestamp": "2024-01-15T10:30:45Z",
  "packages_processed": 15,
  "average_delivery_time": 240,
  "route_efficiency": 92,
  "details": "Route to Regional Hub A optimized"
}

Please generate the complete Python script for Minecraft Code Builder.
Include error handling and the ability to stop with the "stop_deliveries" command.
```

---

## 🛠️ Step-by-Step Process

### Step 1: Choose Your Scenario
Select one of the pre-built scenarios above OR customize the template with your own details.

### Step 2: Prepare Your Minecraft Environment
- Launch Minecraft Education Edition
- Create a new world (Flat world recommended)
- Enter Code Builder by pressing 'C'
- Create a new project

### Step 3: Generate Code with Copilot
- Open VS Code
- Open **GitHub Copilot Chat** (Ctrl+Shift+I)
- Copy and paste your customized prompt
- Copilot will generate the complete script

### Step 4: Copy to Minecraft
- Copy the generated Python code
- Paste into Minecraft Code Builder
- Run the code to build your environment

### Step 5: Execute the Agent
- Return to Minecraft chat
- Type your trigger command (e.g., `run_shift`)
- The agent will start generating events
- Events will be prefixed with "FABRIC_EVENT|"

### Step 6: Verify EventStream Connection
- Open your Fabric Eventstream
- Check that events are arriving
- Verify JSON structure matches your schema

---

## 📊 Event Schema Template

All events should follow this structure:

```json
{
  "event_type": "string - identifier for event type",
  "agent_name": "string - name of the agent",
  "location": "string - zone/location in warehouse",
  "timestamp": "ISO 8601 format - YYYY-MM-DDTHH:MM:SSZ",
  "your_metric_1": "number or string",
  "your_metric_2": "number or string",
  "your_metric_3": "number or string",
  "details": "string - optional additional context"
}
```

---

## 🎯 Customization Tips

### Adding More Zones
Increase complexity by defining more zones:
```python
zones = {
    "zone_a": {"x_min": 100, "x_max": 120, "description": "Area A"},
    "zone_b": {"x_min": 130, "x_max": 150, "description": "Area B"},
    # Add as many as needed
}
```

### Adding More Metrics
Track additional business metrics:
```python
# Add to your events:
"efficiency_score": calculate_efficiency(),
"quality_score": calculate_quality(),
"cost_per_unit": calculate_cost(),
```

### Changing Event Frequency
Modify the timing in your prompt:
- Every 2 seconds = high-frequency, high-volume data
- Every 10 seconds = moderate frequency, less storage
- Every 30 seconds = low-frequency, summary data

### Adding Randomness
Make your simulation more realistic:
```python
import random
"metric": random.randint(80, 120),  # Random value
"success_rate": 0.95 + random.uniform(-0.05, 0.05),  # Varies slightly
```

---

## 🔗 Integration Points

After generating your custom agent:

1. **EventStream Connection**: Events must be sent via WebSocket with "FABRIC_EVENT|" prefix
2. **KQL Processing**: Events are parsed and stored in Eventhouse tables
3. **Semantic Model**: Data is transformed for analytics
4. **Fabric App**: Real-time dashboard displays the metrics

See [03-EVENTSTREAM-SETUP.md](../docs/03-EVENTSTREAM-SETUP.md) for connection details.

---

## 📝 Testing Your Prompt

Before using in production:

1. Generate code with Copilot
2. Review for:
   - Correct event_type naming
   - Valid JSON formatting
   - Proper timestamp generation
   - Metric data types
3. Run in test world first
4. Verify events appear in EventStream
5. Check KQL table for correct parsing

---

## 💡 Pro Tips

✅ **Start Simple**: Begin with 1-2 metrics, expand gradually

✅ **Test Events**: Run a short test before long simulation

✅ **Monitor Costs**: High-frequency events = higher Azure costs

✅ **Version Control**: Keep your prompts in Git for reproducibility

✅ **Iterate**: Test → Adjust → Improve your agent behavior

---

## 🆘 Common Issues

**Q: Generated code has syntax errors**
- Copilot may need refinement. Ask: "Fix syntax errors and add comments"

**Q: Events aren't appearing in EventStream**
- Ensure "FABRIC_EVENT|" prefix is present in chat messages
- Check fabric_bridge.py is running

**Q: JSON parsing fails**
- Validate JSON format: Test in [jsonlint.com](https://jsonlint.com)
- Ensure proper escaping of special characters

**Q: Metrics don't make sense**
- Adjust the calculation logic in your prompt
- Add validation checks

---

## 📚 Next Steps

Once your custom agent is working:
1. Connect to Fabric EventStream (see [03-EVENTSTREAM-SETUP.md](../docs/03-EVENTSTREAM-SETUP.md))
2. Create KQL table for your event type (see [04-EVENTHOUSE-SETUP.md](../docs/04-EVENTHOUSE-SETUP.md))
3. Build semantic model for your metrics (see [05-SEMANTIC-MODEL.md](../docs/05-SEMANTIC-MODEL.md))
4. Create dashboard in Fabric App (see [06-FABRIC-APP.md](../docs/06-FABRIC-APP.md))

---

**Happy customizing! 🚀**
