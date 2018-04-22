import cv2
import time
def take_picture():
    cap = cv2.VideoCapture(0)

    while(1):
        cap.set(cv2.CAP_PROP_AUTOFOCUS, True)
        #cap.set(cv2.CAP_PROP_POS_MSEC, True)
        ret, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

        cv2.imshow('frame', rgb)
        out = cv2.imwrite('hello.jpg', frame)
        #img = cv2.imread('hello.jpg',0)
        #cv2.imshow('image', img)
        time.sleep(2)
        break

    cap.release()
    cv2.destroyAllWindows()
    
    


