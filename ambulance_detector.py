import torch
import cv2
import time
import requests

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
model.conf = 0.4

AMBULANCE_KEYWORDS = ['ambulance']

# Flask server URL
SERVER_URL = 'http://127.0.0.1:5000/update_detection'  # Change to public IP when deploying on VPS

video_path = 'media/Ambulance-demo.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

print("🚑 Starting Ambulance Detection...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    labels = results.pandas().xyxy[0]['name']

    ambulance_detected = any(label.lower() in AMBULANCE_KEYWORDS for label in labels)

    results.render()
    frame = results.ims[0]

    if ambulance_detected:
        print("🚨 Ambulance Detected!")
        try:
            response = requests.post(SERVER_URL, json={"detected": True})
            print("→ Server Response:", response.text)
        except requests.exceptions.RequestException as e:
            print("⚠️ Failed to notify server:", e)

        time.sleep(3)

    cv2.imshow("Ambulance Detector", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("🔁 Detection ended.")
