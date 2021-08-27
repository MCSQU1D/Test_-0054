import pygame
from time import sleep
from time import perf_counter
import random
import os
import math
import threading
from operator import itemgetter, attrgetter


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

class atom:
    def __init__(self, x_position, y_position, type):
        self.x_position = x_position
        self.y_position = y_position
        self.type = type
        self.x_velocity = 0
        self.y_velocity = 0
        self.colour = Atom_Dict[type]["Colour"]


    def display_atom(self):
        pass
        rect = pygame.Rect(self.x_position, self.y_position, 1, 1)
        pygame.draw.rect(screen, (self.colour), rect)


def SimulatorMousePressedAdd(size):
    mx,my = pygame.mouse.get_pos()
    for i in range(-round(size/2)-1,round(size/2)+1):
        for j in range(-round(size/2)-1,round(size/2)+1):
            atoms.append(atom(mx+i, my+j, "Na"))


def SimulatorMousePressedRemove(size):
    mx,my = pygame.mouse.get_pos()
    atomdeletelist=[]
    for i in range(len(atoms)):
        if atoms[i].x_position >= mx-round(cursor_size/2)-1 and atoms[i].x_position <= mx+round(cursor_size/2)+1 and atoms[i].y_position >= my-round(cursor_size/2)-1 and atoms[i].y_position <= my+round(cursor_size/2)+1:
            atomdeletelist.append(atoms[i])
    for i in atomdeletelist:
        atoms.remove(i)
        del i


def Rendering_Particles():
    screen.fill((0,0,0))  # (R, G, B)

    if pygame.mouse.get_pressed()[0] == 1:
        SimulatorMousePressedAdd(cursor_size)
        #pass

    if pygame.mouse.get_pressed()[2] == 1:
        SimulatorMousePressedRemove(cursor_size)

    mx,my = pygame.mouse.get_pos()
    CreateButton(mx-round(cursor_size/2)-1,my-round(cursor_size/2)-1,mx+round(cursor_size/2)+1,my+round(cursor_size/2)+1, "Cursor")

    for i in range(len(atoms)):
        atoms[i].display_atom()



### PHYSICS START ###


def Physics():
    for i in range(len(atoms)):

        #BORDERS 10, 10, 900, 500
        if atoms[i].x_position > 900:
            atoms[i].x_position = 900
            atoms[i].x_velocity = 0

        if atoms[i].x_position < 10:
            atoms[i].x_position = 10
            atoms[i].x_velocity = 0

        if atoms[i].y_position > 500:
             atoms[i].y_position = 500
             atoms[i].y_velocity = 0

        if atoms[i].y_position < 10:
            atoms[i].y_position = 10
            atoms[i].y_velocity = 0

        atoms[i].x_velocity = atoms[i].x_velocity + (1/1)*random.randrange(-1, 1+1)
        atoms[i].y_velocity = atoms[i].y_velocity + (1/8)*random.randrange(-1, 1+1)
        atoms[i].y_velocity = atoms[i].y_velocity + (9.8 * 1/60)  # v = u + at

        atoms[i].y_position = atoms[i].y_position + atoms[i].y_velocity
        atoms[i].x_position = atoms[i].x_position + atoms[i].x_velocity
        atoms[i].y_position = round(atoms[i].y_position)
        atoms[i].x_position = round(atoms[i].x_position)
        atoms[i].x_velocity = 0

        Coordinate_Holder = atoms[i].x_position, atoms[i].y_position
        coordinates.append(Coordinate_Holder)

    btoms = sorted(atoms, key=sortx_position)
    for i in range(len(atoms)):                     #Should check only when there is movement, and only on the particles that move
        if btoms[i].y_position == btoms[i-1].y_position and btoms[i].x_position == btoms[i-1].x_position and btoms[i] != btoms[i-1]:
            Stacking(btoms[i],btoms[i-1])
            btoms = sorted(atoms, key=sortx_position)

        if contains(atoms, lambda x: x.x_position == atoms[i].x_position, lambda x: x.y_position == atoms[i].y_position, i):
            Stacking(atoms[i],atoms[i-1])
            btoms = sorted(atoms, key=sortx_position)

def contains(list, filter_x, filter_y, atomnumber):
    for x in list:
        if filter_x(x) and filter_y(x) and x != list[atomnumber]:
            return True
    return False


def Stacking(atom_A, atom_B):
    atom_A.y_velocity = 0
    atom_A.y_position -= 1



def CheckContact(atom_1, atom_2):
    atom_1CheckY1 = atom_1.y_position - 1
    atom_1CheckY2 = atom_1.y_position + 1
    atom_1CheckX1 = atom_1.x_position - 1
    atom_1CheckX2 = atom_1.x_position + 1

    if atom_2.y_position >= atom_1CheckY1 and atom_2.y_position <= atom_1CheckY2 and atom_2.x_position >= atom_1CheckX1 and atom_2.x_position <= atom_1CheckX2:
        return True

def sortx_position(self):
    return self.x_position

def sorty_position(self):
    return self.y_position


### PHYSICS END ###


### SEPERATE PHYSICS LOOP FROM RENDERING ###


### MAIN LOOP ###

pygame.mouse.set_visible(False)
screen.fill((0,0,0))  # (R, G, B)



a = 0
cursor_size = 4
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    threads = []
    Threading_Rendering_Particles = threading.Thread(target=Rendering_Particles)
    threads.append(Threading_Rendering_Particles)
    Threading_Rendering_Particles.start()

    Threading_Physics = threading.Thread(target=Physics)
    threads.append(Threading_Physics)
    Threading_Physics.start()

    ### CONSIDER LOCKING VARIABLES THAT ARE SHARED https://docs.python.org/3/library/threading.html#lock-objects and https://realpython.com/intro-to-python-threading/


    pygame.display.update()
    clock.tick(60)
    end = perf_counter()
    FPS = (round(1/(end-start),2))
    print("FPS: " + str(FPS))
    start = perf_counter()
    print("PARTICLES: " + str(len(atoms)))

#pygame.quit()
