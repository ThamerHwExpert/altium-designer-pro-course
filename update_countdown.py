#!/usr/bin/env python3
import datetime
import json

# Read the deadline from file (assumed in ISO format)
with open('deadline.txt', 'r') as f:
    deadline_str = f.read().strip()

# Parse the deadline
deadline = datetime.datetime.fromisoformat(deadline_str.replace("Z", "+00:00"))
now = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)

# Calculate remaining time (you can output days or hours, here we choose hours)
remaining = deadline - now
hours_left = int(remaining.total_seconds() // 3600) if remaining.total_seconds() > 0 else 0

# Create the JSON structure for Shields.io
data = {
    "schemaVersion": 1,
    "label": "Deadline",
    "message": f"{hours_left} hours left",
    "color": "blue"
}

# Write the JSON file
with open('countdown.json', 'w') as f:
    json.dump(data, f)
