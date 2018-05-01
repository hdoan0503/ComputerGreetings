import cv2
import numpy as np

#import the RGB_Checker on github
import RGB_Checker as f

# Change BGR ->HSV
#green = np.uint8([[[0,255,0 ]]])
#hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
# print ("hsv green: ")
# print hsv_green
# Change HSV into RGB
#greenHSV = np.uint8([[[60,255,255]]])
#rgb_green = cv2.cvtColor(greenHSV,cv2.COLOR_HSV2BGR)
# print ("rgb green: ")
# print rgb_green

# Change a BGR value into HSV
#test = np.uint8([[[70,20,8 ]]])
#hsv_test = cv2.cvtColor(test,cv2.COLOR_BGR2HSV)
# print ("hsv test: ")
#print hsv_test

# Testing
# Test how lists work with adding elements from a numpy array.
#colorList = [test[0,0,0], test[0,0,1], test[0,0,2]]
def color_picker():
#call the RGB color from picture
    rgb = f.RGB_picker()
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]

    #convert them to HSV
    np_color = np.uint8([[[r,g,b]]])
    color = cv2.cvtColor(np_color,cv2.COLOR_RGB2HSV)
    #print(type(color))
    print(color)
    # Takes in a list of 3 HSV values and sorts them based on their approximate color shade.

        # Red-> Orange
    if(color[0,0,0] >= 0 and color[0,0,0] <= 25 and color[0,0,1] >= 40 and color[0,0,1] <=255 and color[0,0,2] >= 40 and color[0,0,2] <=255):
        print("red")
        color = 'red'
        # Yellow
    elif(color[0,0,0] >= 25 and color[0,0,0] <= 40 and color[0,0,1] >= 40 and color[0,0,1] <=255 and color[0,0,2] >= 40 and color[0,0,2] <=255):
        print("yellow")
        color = 'yellow'
        # Green
    elif(color[0,0,0] >= 40 and color[0,0,0] <= 85 and color[0,0,1] >= 40 and color[0,0,1] <=255 and color[0,0,2] >= 40 and color[0,0,2] <=255):
        print("green")
        color = 'green'
        # Blue
    elif(color[0,0,0] >= 85 and color[0,0,0] <= 120 and color[0,0,1] >= 40 and color[0,0,1] <=255 and color[0,0,2] >= 40 and color[0,0,2] <=255):
        print("blue")
        color = 'blue'
        #Pink->Purple
    elif(color[0,0,0] >= 120 and color[0,0,0] <= 160 and color[0,0,1] >= 40 and color[0,0,1] <=255 and color[0,0,2] >= 40 and color[0,0,2] <=255):
        print("pink")
        color = 'pink'
        # Black
    elif(color[0,0,0] >= 0 and color[0,0,0] <= 180 and color[0,0,1] >= 0 and color[0,0,1] <=255 and color[0,0,2] >= 0 and color[0,0,2] <=30):
        print("black")
        color = 'black'
    else:
        print("No Color")
        color = 'No Color'

    return color






