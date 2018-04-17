import numpy as np
import cv2
from PIL import Image
def RGB_picker():
    i = cv2.imread('10.jpeg')
    img = cv2.resize(i, (540, 960))

    Z = img.reshape((-1,3))

    # convert to np.float32
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 3
    ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))

    #cv2.imshow('res2',res2)

    #rewrite the picture and save it as test.jpg
    cv2.imwrite('test.jpg', res2)
    test = Image.open('test.jpg')
    w, h = test.size

    #make a list of all RGB number which is appearing on the picture
    list = test.getcolors(w * h)
    #sort the list
    list.sort()

    #create a variable to store the closest RBG color's number
    most_frequent_pixel = list[-1]

    for count, colour in list:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)

    print most_frequent_pixel[1]
    #print test.getcolors(w * h)

    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return most_frequent_pixel[1]

