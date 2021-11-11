import numpy as np
import cv2

cap = cv2.VideoCapture('http://10.0.0.100:4747/video')

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0,height), (width, 0), (0,255,0),10)
    img = cv2.line(frame, (0,0), (width, height), (0,255,0),10)
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 30), 5)
    img = cv2.circle(img, (300,300), 60, (0, 0, 255), -1)
    font = cv2.FONT_HERSHEY_PLAIN
    img = cv2.putText(img, 'Joao e o cara', (200, height -10), font, 3, (0, 0, 0), 5, cv2.LINE_AA)
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
