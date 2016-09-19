
import pygame, sys
from pygame.locals import *
import math

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((600, 400), 0, 32)
pygame.display.set_caption('STUDY')
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
GREY =  (166, 166, 166)

pygame.mixer.music.load('bg.mp3')

#text printing function
def printText(txtText, Textfont, Textsize , Textx, Texty, Textcolor):
	myfont = pygame.font.SysFont(Textfont, Textsize)
	label = myfont.render(txtText, 1, Textcolor)
	DISPLAYSURF.blit(label, (Textx, Texty))

bg = pygame.image.load('bg.jpg')

class Clickable():
    def __init__(self, x, y, w, h, text, function):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.text = text
        self.function = function
    def mouse_events(self):
        pass
    def render(self):
        pass

def main_menu():
    
    while True: 
        DISPLAYSURF.blit(bg,(0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        printText('PLAY', 'comicsans', 30, 120, 125, GREY)
        printText('EXIT', 'comicsans', 30, 540, 300, GREY)  
        printText('SETTINGS', 'comicsans', 30, 410, 100, GREY)
        printText('LOAD', 'comicsans', 30, 135, 330, GREY) 
        pygame.display.update()
        fpsClock.tick(FPS)

pygame.mixer.music.play(-1)
main_menu()
