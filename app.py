from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route("/api")
def countdown():
    # Set your deadline here (year, month, day, hour, minute, second)
    deadline = datetime.datetime(2025, 4, 4, 0, 0, 0)
    now = datetime.datetime.utcnow()
    diff = deadline - now
    days_left = diff.days if diff.days > 0 else 0

    # Return JSON in the format Shields.io expects
    return jsonify({
        "schemaVersion": 1,
        "label": "Deadline",
        "message": f"{days_left} days left",
        "color": "blue"
    })

if __name__ == "__main__":
    app.run(debug=True)
