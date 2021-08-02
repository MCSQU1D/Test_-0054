import pygame
from time import sleep
from time import perf_counter
import random
import os
import math
from multiprocessing import Process
from operator import itemgetter, attrgetter
import numpy as np


pygame.init()

atoms = []
atomsRect = []

### SCREEN AND CLOCK ###
display_width = 960
display_height = 540
screen = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
screen.fill((0,0,0))  # (R, G, B)


### VARIABLE DECLARATION ###

start = 0
end = 0
### FUNCTIONS ###
def CreateButton(x1,y1,x2,y2,name):
    #global Selected_Molecule
    #buttonsDict[(x1, x2, y1, y2)] = name
    pygame.draw.rect(screen, (255,255,255), (x1,y1,x2-x1,y2-y1))
    pygame.draw.rect(screen, (0,0,0), (x1+1,y1+1,x2-x1-2,y2-y1-2))
    #if name == Selected_Molecule:
    #    pygame.draw.rect(screen, (0,0,0), (x1,y1,x2-x1,y2-y1))
    #    pygame.draw.rect(screen, (255,255,255), (x1+1,y1+1,x2-x1-2,y2-y1-2))
    #if name not in ["InformationPanel", "WorkSpace", "Cursor"]:
    #    PrintText((x1+x2)/2,(y1+y2)/2,name,'Apple II Pro.otf',12)

Atom_List = ["H", "He", "C", "N", "O", "Na", "Al", "Fe", "Au", "H20"]
Atom_Dict = {
    "H" : {
    "Colour" : (150,200,255),
    "State" : "Gas",
    },
    "He" : {
    "Colour" : (250,250,150),
    "State" : "Gas",
    },
    "C" : {
    "Colour" : (140,140,140),
    "State" : "Solid",
    },
    "N" : {
    "Colour" : (130,225,115),
    "State" : "Gas",
    },
    "O" : {
    "Colour" : (100, 150, 200),
    "State" : "Gas",
    },
    "Na" : {
    "Colour" : (200,200,200),
    "State" : "Solid",
    },
    "Al" : {
    "Colour" : (160,160,160),
    "State" : "Solid",
    },
    "Fe" : {
    "Colour" : (150,140,140),
    "State" : "Solid",
    },
    "Au" : {
    "Colour" : (170,170,80),
    "State" : "Solid",
    },
    "H20" : {
    "Colour" : (0,0,255),
    "State" : "Liquid",
    }
}

coordinates = []










screen.fill((0,0,0))  # (R, G, B)


cursor_size = 4
running = False
while running == True:
    screen.fill((0,0,0))  # (R, G, B)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    if pygame.mouse.get_pressed()[0] == 1:
        #SimulatorMousePressedAdd(cursor_size)
        pass

    if pygame.mouse.get_pressed()[2] == 1:
        #SimulatorMousePressedRemove(cursor_size)
        pass

    # updates the display
    pygame.display.update()
    # clock.tick(framespersecond)
    clock.tick(60)
    end = perf_counter()
    FPS = (round(1/(end-start),2))
    print("FPS: " + str(FPS))
    start = perf_counter()
    print("PARTICLES: " + str(len(atoms)))

#pygame.quit()
