import pygame
import random
pygame.mixer.init()
def play_randomSong():
    #create a list of file names
    musicFiles = ['random1', 'random2', 'random3']

    #create `variable contain String for file extension.
    musicEx = '.mp3'

    #random the music
    finalMusic = random.choice(musicFiles)

    #play the music
    pygame.mixer.music.load(finalMusic + musicEx)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

