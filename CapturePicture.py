import cv2
import time

cap = cv2.VideoCapture(0)

while(1):
    cap.set(cv2.CAP_PROP_AUTOFOCUS, True)
    cap.set(cv2.CAP_PROP_POS_MSEC, True)
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    time.sleep(2) #set time for turn off the camera
    out = cv2.imwrite('hello.jpg', frame)
    break
cap.release()
cv2.destroyAllWindows()


