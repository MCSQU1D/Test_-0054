

import pygame
from time import sleep
from time import perf_counter
import random
import os
import math
from multiprocessing import Process


pygame.init()

atoms = []

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

class atom:
    def __init__(self, x_position, y_position, colour, type):
        self.x_position = x_position
        self.y_position = y_position
        self.type = type
        self.x_velocity = 0
        self.y_velocity = 0
        self.colour = colour


    def gravity(self):
        self.y_velocity = self.y_velocity + (9.8 * 1/60)
        for i in atoms:
            if self.x_position == i.x_position:
                if self.y_position + self.y_velocity == i.y_position:
                    #print("Collision")
                    pass
        self.y_position = self.y_position + self.y_velocity

    def display_atom(self):
        pygame.draw.rect(screen, (self.colour), (self.x_position, self.y_position, 1, 1))

    def create_atom(self):
        mx,my = pygame.mouse.get_pos()
        atom = atom(mx, my, (255,255,255), "H2O")



### SEPERATE PHYSICS LOOP FROM RENDERING ###


### MAIN LOOP ###

pygame.mouse.set_visible(False)
screen.fill((0,0,0))  # (R, G, B)
#atom2 = molecule(160, 8, (255,255,255))

a = 0
cursor_size = 4
running = True
while running == True:
    screen.fill((0,0,0))  # (R, G, B)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    if pygame.mouse.get_pressed()[0] == 1:
        mx,my = pygame.mouse.get_pos()
        cursorx = mx-1
        cursory = my-1
        for i in range(-round(cursor_size/2),round(cursor_size/2)+1):
            cursorx += 1
            for j in range(-round(cursor_size/2),round(cursor_size/2)+1):
                cursory += 1
                atoms.append(atom(mx+i, my+j, (255,255,255), "H2O"))
            #for i in range(cursor_size)


        #atoms.append(atom(mx, my, (255,255,255), "H2O"))

    mx,my = pygame.mouse.get_pos()
    CreateButton(mx-round(cursor_size/2)-1,my-round(cursor_size/2)-1,mx+round(cursor_size/2)+1,my+round(cursor_size/2)+1, "Cursor")


    if pygame.mouse.get_pressed()[2] == 1:
        mx,my = pygame.mouse.get_pos()
        for i in range(len(atoms)):
            if atoms[i].x_position >= mx-round(cursor_size/2) and atoms[i].x_position <= mx+round(cursor_size/2) and atoms[i].y_position >= my-round(cursor_size/2) and atoms[i].y_position <= my+round(cursor_size/2):
                #print(i)
                print(atoms[i])
                #atoms.remove(atoms[i])




    for i in range(len(atoms)):
        #if i != 0 and atoms[i].y_position == atoms[i-1].y_position and atoms[i].x_position == atoms[i-1].x_position:
            #atoms[i].y_position -= 1
        if atoms[i].y_position < 430:
            atoms[i].gravity()
            atoms[i].x_position = atoms[i].x_position + int(random.uniform(-1.4, 1.4))


        if atoms[i].y_position > 430:
             #atoms.remove(i)
             atoms[i].y_position = 430
        atoms[i].display_atom()


    # updates the display
    pygame.display.update()
    # clock.tick(framespersecond)
    clock.tick(60)
    end = perf_counter()
    FPS = (round(1/(end-start),2))
    print("FPS: " + str(FPS))
    start = perf_counter()

#pygame.quit()
