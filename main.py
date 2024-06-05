import cv2
from picamera2 import Picamera2

cv2.startWindowThread()

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

cap = cv2.VideoCapture(0)

while True: 
    frame = picam2.capture_array()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    cv2.imshow("Video Output", blur)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
