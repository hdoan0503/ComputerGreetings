import numpy as np
import cv2
from PIL import Image
def RGB_picker():
    # Read in an image for testing
    i = cv2.imread('hello.jpg')
    img = cv2.resize(i, (720, 1280))

    Z = img.reshape((-1,3))

    # convert to np.float32
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans clustering formula to detect most dominant colors
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    # K is how many clusters to have in an image. (How many dominant colors to be used)
    K = 3
    ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    #Pop up kmeans result (Not formatted well)
    cv2.imshow('res2',res2)

    #rewrite the picture and save it as test.jpg
    cv2.imwrite('test.jpg', res2)
    test = Image.open('test.jpg')
    w, h = test.size


    # Print's all colors in an image to the console
    #print test.getcolors(w * h)
    k = cv2.waitKey(2000)
    cv2.destroyAllWindows()

    #create a variable to store the first RBG color's number
        #make a list of all RGB number which is appearing on the picture
    list = test.getcolors(w * h)
    #sort the list
    list.sort()
    most_frequent_pixel = list[-1]

    for count, colour in list:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)
    #print most_frequent_pixel[1]
    return most_frequent_pixel[1]








