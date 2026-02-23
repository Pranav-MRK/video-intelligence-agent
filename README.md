# video-intelligence-agent
Structure:

video-intelligence-agent/
│
├── app/
│   ├── agent.py
│   ├── camera.py
│   └── utils.py
│
├── models/
│
├── logs/
│
├── requirements.txt
├── README.md
└── .gitignore



# Day 1
## Day 1 Progress

- Virtual environment setup
- Basic project structure created
- Camera module implemented
- Agent entry point created
- Live video feed working

# Detector
# When YOLO processes an image, it doesn't just return a name like "person"; it returns a specialized data structure (a tensor).


cls = int(box.cls[0]). idetefiyes what object is , this is a list (or a 1D tensor) containing the class index. YOLO uses numbers to represent objects (e.g., 0 for person, 1 for bicycle, 2 for car).


conf = float(box.conf[0]).  how confident model is  it show that 
box.conf: Short for "confidence." This is a value between 0.0 and 1.0.

[0]: Again, we grab the specific value for this bounding box.

float(...): We convert the tensor value into a standard Python float.

Example: If conf is 0.92, the model is 92% sure the object is what it claims it is.



for (x1, y1, x2, y2, conf) in detections:
            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.putText(frame, "Person", (x1, y1-10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)


# cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
frame: The background image you are drawing on.

(x1, y1): The starting point (Top-Left corner).

(x2, y2): The ending point (Bottom-Right corner).

(0, 255, 0): The color in BGR format. In OpenCV, this is Pure Green (0 Blue, 255 Green, 0 Red).

2: The thickness of the line in pixels.


# cv2.putText(frame, "Person", (x1, y1-10),
# cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)
"Person": The string of text to display.

(x1, y1-10): The location of the text. By subtracting 10 from y1, we place the text 10 pixels above the top of the bounding box so it doesn't overlap the person's head.

cv2.FONT_HERSHEY_SIMPLEX: The font style (a standard, clean OpenCV font).

0.6: The font scale (size).

(0, 255, 0), 2: Again, the color (Green) and the thickness of the text strokes.