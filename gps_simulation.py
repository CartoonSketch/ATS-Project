
# gps_simulation.py

import time
import requests

# Simulated GPS coordinates of the ambulance moving towards hospital
route_coordinates = [
    (28.6139, 77.2090),  # Start point
    (28.6150, 77.2100),
    (28.6165, 77.2115),
    (28.6180, 77.2130),
    (28.6195, 77.2145),  # Destination
]

SERVER_URL = "http://127.0.0.1:5000/update_gps"  # Updated endpoint

def send_gps_data():
    print("📍 Starting GPS Simulation for Ambulance...")

    for lat, lng in route_coordinates:
        data = {
            "lat": lat,
            "lng": lng
        }

        try:
            response = requests.post(SERVER_URL, json=data)
            print(f"✅ Sent GPS: {lat}, {lng} → Server: {response.text}")
        except requests.exceptions.RequestException as e:
            print("⚠️ Failed to send GPS data:", e)

        time.sleep(2)

    print("🏁 GPS simulation completed.")

if __name__ == "__main__":
    send_gps_data()
