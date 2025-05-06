import torch    # type: ignore
import cv2     
from map_alert import send_map_alert

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
animal_classes = ['cow', 'sheep', 'dog', 'horse', 'cat', 'bird', 'elephant', 'bear', 'zebra', 'giraffe']

cap = cv2.VideoCapture(r'C:\Users\SANDHU PC\Downloads\Sheep video.mp4')

alert_sent = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret or frame is None:
        break

    results = model(frame)
    detections = results.pandas().xyxy[0]

    animal_detected = False
    for _, row in detections.iterrows():
        label = row['name']
        if label in animal_classes:
            animal_detected = True
            x1, y1, x2, y2 = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    if animal_detected and not alert_sent:
        send_map_alert()
        print("✅ Map alert sent.")
        alert_sent = True

    cv2.imshow('Animal Detection', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
