# flask_server/app.py

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Store detected ambulances and their last known GPS location
ambulance_locations = {}

@app.route('/')
def index():
    return jsonify({"message": "Ambulance Traffic Management API Running"})

@app.route('/update', methods=['POST'])
def update_ambulance_status():
    data = request.json

    ambulance_id = data.get("ambulance_id")
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    detected = data.get("detected")  # True or False

    if not all([ambulance_id, latitude, longitude]) or detected is None:
        return jsonify({"status": "error", "message": "Missing required fields"}), 400

    ambulance_locations[ambulance_id] = {
        "latitude": latitude,
        "longitude": longitude,
        "detected": detected,
        "timestamp": datetime.now().isoformat()
    }

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Ambulance {ambulance_id} {'DETECTED' if detected else 'CLEARED'} at ({latitude}, {longitude})")

    return jsonify({"status": "success", "message": "Ambulance data updated"})

@app.route('/get_status', methods=['GET'])
def get_status():
    return jsonify(ambulance_locations)

if __name__ == '__main__':
    app.run(debug=True)
