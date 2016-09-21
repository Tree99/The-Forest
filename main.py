
import pygame, sys
from pygame.locals import *
import math

pygame.init()

FPS = 30 
fpsClock = pygame.time.Clock()

window_width = 600
window_height = 400

# set up the window
DISPLAYSURF = pygame.display.set_mode((window_width, window_height), 0, 32)
pygame.display.set_caption('STUDY')
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
GREY =  (166, 166, 166)

pygame.mixer.music.load('bg.mp3')

def printText(txtText, Textfont, Textsize , Textx, Texty, Textcolor):
	myfont = pygame.font.SysFont(Textfont, Textsize)
	label = myfont.render(txtText, 1, Textcolor)
	DISPLAYSURF.blit(label, (Textx, Texty))

bg = pygame.image.load('bg.jpg')
mousex, mousey = 0, 0

class Clickable():
    def __init__(self, x, y, w, h, text, function, font_size, color):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.text = text
        self.function = function
        self.font_size, self.color = font_size, color
    def check_mouse_hovering(self):
        if (mousex > self.x and mousex < self.x + self.w and
        mousey > self.y and mousey < self.y + self.h):
            return True
        return False
    def render(self):
        if self.check_mouse_hovering():
            self.color = WHITE
        else:
            self.color = GREY
        # pygame.draw.rect(DISPLAYSURF, WHITE, (self.x, self.y, self.w, self.h), 0)
        printText(self.text, 'comicsans', self.font_size, self.x, self.y, self.color)

def main_menu():
    global mousex, mousey
    clickable_things = [Clickable(120, 125, 50, 18, 'PLAY', play, 30, GREY),
                        Clickable(410, 100, 100, 18, 'SETTINGS', play, 30, GREY),
                        Clickable(540, 300, 47, 18, 'EXIT', e_xit, 30, GREY),
                        Clickable(135, 330, 58, 18, 'LOAD', play, 30, GREY)]
    while True: 
        DISPLAYSURF.blit(bg,(0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type is KEYDOWN and event.key == K_f):
                if DISPLAYSURF.get_flags() & FULLSCREEN:
                    pygame.display.set_mode((window_width, window_height),0,32)
                else:
                    pygame.display.set_mode((window_width, window_height), FULLSCREEN)
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                for c in clickable_things:
                    if c.check_mouse_hovering() == True:
                        return c.function()
        for each in clickable_things:
            each.render()
                

        pygame.display.update()
        fpsClock.tick(FPS)

def play():
    pass

def settings():
    pass

def e_xit():
    pygame.quit()
    sys.exit()

pygame.mixer.music.play(-1)
main_menu()
