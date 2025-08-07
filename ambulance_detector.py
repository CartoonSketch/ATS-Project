# ambulance_detector.py

import torch
import cv2
import time
import requests

# Load YOLOv5 model (you must have YOLOv5s or custom-trained ambulance model)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Use 'custom' if you trained your own

# Optional: Set model confidence threshold
model.conf = 0.4

# Define labels that indicate ambulance (in custom models, use class name 'ambulance')
AMBULANCE_KEYWORDS = ['ambulance']

# Flask server URL to notify when ambulance is detected
SERVER_URL = 'http://127.0.0.1:5000/ambulance_detected'

# Load video
video_path = 'media/traffic_video.mp4'  # Replace with your own video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

print("🚑 Starting Ambulance Detection...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Inference
    results = model(frame)
    labels = results.pandas().xyxy[0]['name']

    # Check if ambulance is detected in the frame
    ambulance_detected = any(label.lower() in AMBULANCE_KEYWORDS for label in labels)

    # Draw bounding boxes
    results.render()
    frame = results.ims[0]

    if ambulance_detected:
        print("🚨 Ambulance Detected!")
        try:
            response = requests.post(SERVER_URL, json={"status": "ambulance_detected"})
            print("→ Server Response:", response.text)
        except requests.exceptions.RequestException as e:
            print("⚠️ Failed to notify server:", e)

        # Optional: Slow down processing to simulate real alert time
        time.sleep(3)

    # Show frame
    cv2.imshow("Ambulance Detector", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("🔁 Detection ended.")
