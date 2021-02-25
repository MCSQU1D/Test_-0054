

import pygame
from time import sleep
import random
import os
import math
from multiprocessing import Process


pygame.init()



### SCREEN AND CLOCK ###
display_width = 960
display_height = 540
screen = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
screen.fill((0,0,0))  # (R, G, B)


### VARIABLE DECLARATION ###


### FUNCTIONS ###

class atom:
    def __init__(self, x_position, y_position, colour):
        self.x_position = x_position
        self.y_position = y_position
        self.x_velocity = 0
        self.y_velocity = 0
        self.colour = colour


    def gravity(self):
        self.y_velocity = self.y_velocity + (9.8 * 1/60)
        self.y_position = self.y_position + self.y_velocity

    def display_atom(self):
        pygame.draw.rect(screen, (self.colour), (self.x_position, self.y_position, 4, 4))


class molecule(atom):
    pass


### MAIN LOOP ###


screen.fill((0,0,0))  # (R, G, B)
#atom2 = molecule(160, 8, (255,255,255))
atom1 = molecule(360, 8, (255,255,255))

running = True
while running == True:
    screen.fill((0,0,0))  # (R, G, B)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx,my = pygame.mouse.get_pos()
            atom1 = molecule(mx, my, (255,255,255))


    atom1.gravity()
    atom1.display_atom()

    # updates the display
    pygame.display.update()
    # clock.tick(framespersecond)
    clock.tick(60)

#pygame.quit()
