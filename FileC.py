import pygame
from time import sleep
from time import perf_counter
import random
import os
import math
from multiprocessing import Process


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


class atom:
    def __init__(self, x_position, y_position, colour, type):
        self.x_position = x_position
        self.y_position = y_position
        self.type = type
        self.x_velocity = 0
        self.y_velocity = 0
        self.colour = colour

    def gravity(self):
        self.y_velocity = self.y_velocity + (9.8 * 1/60)  # v = u + at
        self.y_position = self.y_position + self.y_velocity
        self.x_position = self.x_position + self.x_velocity

    def display_atom(self):
        pass
        #self.pygame.Rect(self.x_position, self.y_position, 1, 1)
        #pygame.draw.rect(screen, (self.colour), Temporary_Holder)
        #atomsRect.append(Temporary_Holder)



def SimulatorMousePressedAdd(size):
    mx,my = pygame.mouse.get_pos()
    for i in range(-round(size/2)-1,round(size/2)+1):
        for j in range(-round(size/2)-1,round(size/2)+1):
            atoms.append(atom(mx+i, my+j, (255,255,255), "H2O"))
            atoms[-1].gravity()

def SimulatorMousePressedRemove(size):
    mx,my = pygame.mouse.get_pos()
    atomdeletelist=[]
    for i in range(len(atoms)):
        if atoms[i].x_position >= mx-round(cursor_size/2) and atoms[i].x_position <= mx+round(cursor_size/2) and atoms[i].y_position >= my-round(cursor_size/2) and atoms[i].y_position <= my+round(cursor_size/2):
            atomdeletelist.append(atoms[i])
    for i in atomdeletelist:
        atoms.remove(i)


def Physics():
    for i in range(len(atoms)):

        if atoms[i].y_velocity > 0:
            atoms[i].x_velocity = atoms[i].x_velocity + (1/4)*random.randrange(-4, 4+1)
            atoms[i].gravity()
            atoms[i].x_velocity = 0

        if atoms[i].y_position > 500:               #BORDERS
             atoms[i].y_position = 500
             atoms[i].y_velocity = 0
        atoms[i].display_atom()


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
        SimulatorMousePressedAdd(cursor_size)
        #pass

    if pygame.mouse.get_pressed()[2] == 1:
        SimulatorMousePressedRemove(cursor_size)
        #pass

            #for i in range(cursor_size)


        #atoms.append(atom(mx, my, (255,255,255), "H2O"))

    mx,my = pygame.mouse.get_pos()
    CreateButton(mx-round(cursor_size/2)-1,my-round(cursor_size/2)-1,mx+round(cursor_size/2)+1,my+round(cursor_size/2)+1, "Cursor")

    #if len(atomsRect) != 0:


    Physics()


    # updates the display
    pygame.display.update()
    # clock.tick(framespersecond)
    clock.tick(60)
    end = perf_counter()
    FPS = (round(1/(end-start),2))
    #print("FPS: " + str(FPS))
    start = perf_counter()

#pygame.quit()
