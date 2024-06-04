import cv2
from picamera2 import Picamera2

cv2.startWindowThread()

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'RGB8888', "size": (640, 480)}))
picam2.start()

cap = cv2.VideoCapture(0)

while True: 
    frame = picam2.capture_array()

    cv2.imshow("Video Output", frame)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()