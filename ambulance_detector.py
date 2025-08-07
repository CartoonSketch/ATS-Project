import torch
import cv2
import time
import requests
import sys

# Set confidence threshold
CONFIDENCE_THRESHOLD = 0.4

# Load YOLOv5 model (from GitHub or local if available)
try:
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True)
except Exception:
    print("⚠️ Could not load YOLOv5 model from GitHub. Make sure you have internet or use local copy.")
    exit()

model.conf = CONFIDENCE_THRESHOLD

# Keywords for detection
AMBULANCE_KEYWORDS = ['ambulance']

# Get server URL from command line or use default
SERVER_URL = sys.argv[1] if len(sys.argv) > 1 else 'http://127.0.0.1:5000/update_detection'

# Load video
video_path = 'media/Ambulance-demo.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ Error: Could not open video.")
    exit()

print("🚑 Starting Ambulance Detection...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    df = results.pandas().xyxy[0]
    labels = df['name'] if not df.empty else []

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

        time.sleep(3)  # Delay after detection

    cv2.imshow("Ambulance Detector", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("🔁 Detection ended.")
