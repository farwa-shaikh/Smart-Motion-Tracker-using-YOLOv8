import cv2
import numpy as np
from ultralytics import YOLO
from playsound import playsound
import threading

# Load Model
model = YOLO("model/yolov8m.pt")

# Restricted Zone Coordinates (Adjust as needed)
restricted_zone = (100, 100, 400, 400)  # x1, y1, x2, y2

def play_alarm():
    threading.Thread(target=lambda: playsound("alert.mp3")).start()

cap = cv2.VideoCapture(0)  # Use 0 for webcam | Add IP for CCTV

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, stream=True)

    # Draw Restricted Zone
    x1, y1, x2, y2 = restricted_zone
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 2)
    cv2.putText(frame, "Farwa", (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 255, 255), 2)

    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls = model.names[int(box.cls[0])]
            confidence = float(box.conf[0])
            x1b, y1b, x2b, y2b = map(int, box.xyxy[0])

            # Draw Detection
            cv2.rectangle(frame, (x1b, y1b), (x2b, y2b), (0, 0, 255), 2)
            cv2.putText(frame, f"{cls} {confidence:.2f}", (x1b, y1b - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

            # Raise Alarm if weapon detected or trespassing
            if confidence > 0.65:
                # Trespassing detection
                if x1 < x1b < x2 and y1 < y1b < y2:
                    cv2.putText(frame, "ALERT: Trespassing!", (50, 50),
                                cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 3)
                    play_alarm()

                # Weapon detection
                if cls in ["gun", "knife", "rifle", "weapon"]:
                    cv2.putText(frame, "ALERT: Weapon Detected!", (50, 100),
                                cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 3)
                    play_alarm()

    cv2.imshow("Smart CCTV Security System", frame)

    if cv2.waitKey(1) == 27:  # ESC to Quit
        break

cap.release()
cv2.destroyAllWindows()