import cv2

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

        cv2.imshow("Live Surveillance Feed", frame)

        # Press q to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
