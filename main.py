import cv2
from picamera2 import Picamera2

cv2.startWindowThread()

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

cap = cv2.VideoCapture(0)

while True: 
    frame = picam2.capture_array()
    image = cv2.rotate(frame, cv2.ROTATE_180)
    cropped = image[320:480,0:640]
    gray = cv2.cvtColor(cropped, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (7,7), 0)
    edges = cv2.Canny(blur, 50, 100)
    lines = cv2.HoughLinesP(edges,1,0.01745,100,minLineLength=100,maxLineGap=10)
    for line in lines:
        x1,y1,x2,y2 = line[0]
        cv2.line(blur,(x1,y1),(x2,y2),(0,255,0),2)
    cv2.imshow("Video Output", blur)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
