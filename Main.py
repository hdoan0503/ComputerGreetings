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
    #Happy.play_happymusic()
    print 'red'
elif(colorPicture == 'blue'):
    #Sad.play_sadmusic()
    print 'blue'
elif(colorPicture == 'yellow'):
    #Happy.play_happymusic()
    print 'yellow'
elif(colorPicture == 'pink'):
    #Happy.play_happymusic()
    print 'pink'
elif(colorPicture == 'green'):
    #Happy.play_happymusic()
    print 'green'
elif(colorPicture == 'black'):
    #Sad.play_sadmusic()
    print 'black'
else:
    print 'Can not define the color. Play random music'
