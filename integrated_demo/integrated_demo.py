# integrated_demo/integrated_demo.py

import subprocess
import threading
import time
import webbrowser

def run_ambulance_detection():
    print("[MODULE] Running ambulance detection...")
    subprocess.call(['python', '../ambulance_detector.py'])

def run_gps_simulation():
    print("[MODULE] Running GPS simulation...")
    subprocess.call(['python', '../gps_simulation.py'])

def run_flask_server():
    print("[MODULE] Starting Flask backend...")
    subprocess.call(['python', '../flask_server/app.py'])

def run_traffic_gui():
    print("[MODULE] Running traffic signal GUI...")
    subprocess.call(['python', '../traffic_signal_gui.py'])

def run_map_visualizer():
    print("[MODULE] Launching route clearance map...")
    subprocess.call(['python', '../route_clearance_map/map_simulator.py'])

if __name__ == "__main__":
    print("=== Integrated Demo: Advanced Traffic System for Ambulance ===\n")

    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=run_flask_server)
    flask_thread.daemon = True
    flask_thread.start()
    time.sleep(2)  # Give server time to start

    # Open browser for Flask interface (optional)
    webbrowser.open("http://127.0.0.1:5000")

    # Run modules sequentially (can be made parallel if needed)
    run_ambulance_detection()
    run_gps_simulation()
    run_traffic_gui()
    run_map_visualizer()

    print("\n[✅] Simulation complete!")
