import cv2
from detector import detect_people 
from utils import check_crowed

def start_camera():
    cap = cv2.VideoCapture(0)  # 0 = laptop webcam

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    print("Camera started. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret: break

        # 1. Get detections and count immediately
        detections = detect_people(frame)
        person_count = len(detections)

        # 2. Draw boxes for EACH person
        for (x1, y1, x2, y2, conf) in detections:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, "Person", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # 3. Draw the GLOBAL count once (Top Left)
        cv2.putText(frame, f"Total People: {person_count}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # 4. Run Alert Logic
        if check_crowed(person_count):
            # Added 'f' before the string to make it an f-string
            print(f"[ALERT] Crowd Detected! Count: {person_count}")    

        cv2.imshow("Live Surveillance Feed", frame)

        # Press q to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


