#!/usr/bin/env python3
import datetime
import json

# Read the deadline from file
with open('deadline.txt', 'r') as f:
    deadline_str = f.read().strip()

# Parse the deadline (assumes ISO format)
deadline = datetime.datetime.fromisoformat(deadline_str.replace("Z", "+00:00"))
now = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)

# Calculate remaining time in days (you can refine this to include hours, etc.)
remaining = deadline - now
days_left = remaining.days if remaining.days >= 0 else 0

# Create a JSON structure for Shields.io
data = {
    "schemaVersion": 1,
    "label": "Deadline",
    "message": f"{days_left} days left",
    "color": "blue"
}

# Write the JSON file
with open('countdown.json', 'w') as f:
    json.dump(data, f)
