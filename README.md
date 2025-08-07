# 🚑 ATS for Path Clearance and Detection of Ambulance

This project simulates an intelligent traffic management system that detects approaching ambulances using video footage, tracks their GPS locations, and clears traffic signals virtually to provide a green corridor to the hospital — **entirely through software**, without any physical hardware.

## 📌 Project Objective

To design a **virtual traffic system** where:
- Ambulance is **automatically detected** using computer vision (YOLOv5).
- Its **live GPS location** is simulated and sent to a Flask server.
- **Traffic signals** are managed to **clear the path** for the ambulance.
- All modules are integrated to demonstrate a working prototype in software.

## 🧱 Project Structure

Advanced-Traffic-System-Ambulance/
│
├── README.md                   
├── ambulance_detector.py        
├── gps_simulation.py            
├── traffic_signal_gui.py        
├── flask_server/   
│   ├── app.py
│   └── requirements.txt
├── route_clearance_map/       
├── integrated_demo/           
└── media/                      

## ⚙️ Technologies Used

- 🔍 YOLOv5 (for ambulance detection)
- 🐍 Python 3.8+
- 🧠 OpenCV
- 🌐 Flask (for backend server)
- 🗺️ Folium / Map APIs (for map path clearance)
- 🖥️ Tkinter / PyQt (for GUI traffic simulation)

## 🚦 Modules Overview

| Module | File | Description |
|--------|------|-------------|
| 1 | `ambulance_detector.py` | Detect ambulance using YOLOv5 in video footage |
| 2 | `gps_simulation.py` | Simulates GPS coordinates and sends to backend |
| 3 | `flask_server/app.py` | Receives GPS data and triggers traffic signal updates |
| 4 | `traffic_signal_gui.py` | Shows visual traffic signals that respond to ambulance |
| 5 | `route_clearance_map/` | Simulates map-based path clearance visualization |
| 6 | `integrated_demo/` | Integrates all modules to show the final system |

## 📷 Sample Output

You can store your demo screenshots and videos in the /media/ folder.


## 🙋‍♂️ Contributors

Akash Pandit

## 📜 License

This project is for academic and educational purposes only.
