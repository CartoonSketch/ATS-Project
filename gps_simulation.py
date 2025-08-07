# gps_simulation.py

import time
import random
import requests

# Simulated GPS coordinates of the ambulance moving towards hospital
# These are just dummy latitude and longitude values
route_coordinates = [
    (28.6139, 77.2090),  # Start point (example: Connaught Place)
    (28.6150, 77.2100),
    (28.6165, 77.2115),
    (28.6180, 77.2130),
    (28.6195, 77.2145),  # Destination (example: Hospital)
]

SERVER_URL = "http://116.202.18.208:5000/gps_data"

def send_gps_data():
    print("📍 Starting GPS Simulation for Ambulance...")

    for lat, lon in route_coordinates:
        data = {
            "latitude": lat,
            "longitude": lon
        }

        try:
            response = requests.post(SERVER_URL, json=data)
            print(f"✅ Sent GPS: {lat}, {lon} → Server: {response.text}")
        except requests.exceptions.RequestException as e:
            print("⚠️ Failed to send GPS data:", e)

        time.sleep(2)  # Simulate movement delay

    print("🏁 GPS simulation completed.")

if __name__ == "__main__":
    send_gps_data()
