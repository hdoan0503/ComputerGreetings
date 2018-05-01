import Color_Test
import CapturePicture
import RGB_Checker
import pygame
import RandomSong

#loading sound
pygame.mixer.init()
music = pygame.mixer.music
timer = pygame.time.Clock()
red = 'redorange.mp3'
blue = 'blue.mp3'
yellow = 'yellow.mp3'
pink = 'PinkPurple.mp3'
green = 'green.mp3'
black = 'black.mp3'
#take the picture
CapturePicture.take_picture()

#After taking the picture, the RGB_checker will run and check the picture
RGB_Checker.RGB_picker()

#Use the RGB number from RGB_Checker class to determine which color is it
colorPicture = Color_Test.color_picker()

if(colorPicture == 'red'):
    print 'red'
    music.load(red)
    music.play()
    while music.get_busy():
        timer.tick(60)

elif(colorPicture == 'blue'):
    print 'blue'
    music.load(blue)
    music.play()
    while music.get_busy():
        timer.tick(60)

elif(colorPicture == 'yellow'):
    print 'yellow'
    music.load(yellow)
    music.play()
    while music.get_busy():
        timer.tick(60)
    
elif(colorPicture == 'pink'):
    print 'pink'
    music.load(pink)
    music.play()
    while music.get_busy():
        timer.tick(60)
elif(colorPicture == 'green'):
    print 'green'
    music.load(green)
    music.play()
    while music.get_busy():
        timer.tick(60)
elif(colorPicture == 'black'):
    print 'black'
    music.load(black)
    music.play()
    while music.get_busy():
        timer.tick(60)
else:
    print 'Can not define the color. Play random music'
    RandomSong.play_randomSong()
