import cv2
from detector import detect_people 

def start_camera():
    cap = cv2.VideoCapture(0)  # 0 = laptop webcam

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    print("Camera started. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame.")
            break

        # 1. GENERATE the data first
        detections = detect_people(frame)

        # 2. USE the data to draw
        for (x1, y1, x2, y2, conf) in detections:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, "Person", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # 3. SHOW the results
        cv2.imshow("Live Surveillance Feed", frame)

        # Press q to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


