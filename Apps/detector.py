from ultralytics import YOLO 

# Load right weight Yolo model
model = YOLO("yolov8n.pt")

def detect_people(frame):
    results = model(frame)

    detection =[]

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            if model.names[cls] == "person" and conf>0.5:
                x1,y1,x2,y2 = map(int,box.xyxy[0])
                detection.append((x1,y1,x2,y2,conf))
                
    return detection
            
