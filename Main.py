import Color_Test
import CapturePicture
import RGB_Checker
#import Happy
#import Sad

#take the picture
CapturePicture.take_picture()

#After taking the picture, the RGB_checker will run and check the picture
RGB_Checker.RGB_picker()

#Use the RGB number from RGB_Checker class to determine which color is it
colorPicture = Color_Test.color_picker()

if(colorPicture == 'red'):
    #play red music
    print 'red'
elif(colorPicture == 'blue'):
    #play blue music
    print 'blue'
elif(colorPicture == 'yellow'):
    #play yellow music
    print 'yellow'
elif(colorPicture == 'pink'):
    #play pink music
    print 'pink'
elif(colorPicture == 'green'):
    #play green music
    print 'green'
elif(colorPicture == 'black'):
    #play black music
    print 'black'
else:
    print 'Can not define the color. Play random music'
