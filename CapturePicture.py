import cv2
def take_picture():
    cap = cv2.VideoCapture(0)

    while(1):
        ret, frame = cap.read()
        #rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        #cap.set(cv2.CAP_PROP_POS_MSEC, True)
        cap.set(cv2.CAP_PROP_AUTOFOCUS, True)
        cv2.imshow('frame', frame)
        out = cv2.imwrite('hello.jpg', frame)
        #img = cv2.imread('hello.jpg',0)
        #cv2.imshow('image', img)
        #wait 2 second (take the picture in 2 secs) before turn off the camera 
        cv2.waitKey(2000)
        break

    cap.release()
    cv2.destroyAllWindows()
    
    


