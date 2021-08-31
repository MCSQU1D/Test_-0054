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
Temperature = 2000
start = 0
end = 0
global atom_delete_list
atom_delete_list = []
global atom_create_list
atom_create_list = []

### FUNCTIONS ###
def CreateCursor(x,y,size):
    pygame.draw.rect(screen, (255,255,255), (x-size/2,y-size/2,size,size),1)    #prints the square cursor

def LoadInformation(file):
    path = os.path.join("files")
    filelist = []

    for r, d, f in os.walk(path):
        for file_finder in f:
            if '.txt' in file_finder:
                filelist.append(file_finder)
    for i in filelist:
        if i == file:
            file_finder = i
    #if file_finder == "chemicalinfomation.txt":
    file_pathname = os.getcwd()+"/files/" +file  #finds the files folder
    file_opened = open(file_pathname,"r")
    file_split = file_opened.read().split("\n")
    return file_split



### PARTICLES START ###

class atom:
    def __init__(self, x_position, y_position, type):
        self.x_position = x_position
        self.y_position = y_position
        self.type = type
        self.x_velocity = 0
        self.y_velocity = 0
        self.colour = Atom_Dict[type]["Colour"]
        self.temperature = 20
        self.state = "solid"



    def display_atom(self):
        pass
        rect = pygame.Rect(self.x_position, self.y_position, 1, 1)
        pygame.draw.rect(screen, (self.colour), rect)


def SimulatorMousePressedAdd(size):
    mx,my = pygame.mouse.get_pos()
    for i in range(-round(size/2)-1,round(size/2)+1):
        for j in range(-round(size/2)-1,round(size/2)+1):
            if mx+i < 900 and mx+i > 10 and my+j > 10 and my+j < 500:
                atoms.append(atom(mx+i, my+j, Selected_Molecule))


def SimulatorMousePressedRemove(size):
    mx,my = pygame.mouse.get_pos()
    atomdeletelist=[]
    for i in range(len(atoms)):
        if atoms[i].x_position >= mx-round(cursor_size/2)-1 and atoms[i].x_position <= mx+round(cursor_size/2)+1 and atoms[i].y_position >= my-round(cursor_size/2)-1 and atoms[i].y_position <= my+round(cursor_size/2)+1:
            atomdeletelist.append(atoms[i])
    for i in atomdeletelist:
        atoms.remove(i)
        del i


def Atom_Manager():
    global atom_delete_list
    global atom_create_list

    for k in atom_delete_list:
        if k in atoms:
            atoms.remove(k)
            del k
    atom_delete_list = []

    for j in atom_create_list:          #atom_create_list.append([atom_1.x_position, atom_1.y_position, f[1], atom_1.x_velocity, atom_1.y_velocity])
        atoms.append(atom(j[0], j[1], j[2]))
        atoms[-1].x_velocity = j[3]
        atoms[-1].x_velocity = j[4]
    atom_create_list = []


def Rendering_Particles():
    screen.fill((0,0,0))  # (R, G, B)

    if pygame.mouse.get_pressed()[0] == 1:
        SimulatorMousePressedAdd(cursor_size)
        #pass

    if pygame.mouse.get_pressed()[2] == 1:
        SimulatorMousePressedRemove(cursor_size)

    mx,my = pygame.mouse.get_pos()
    CreateCursor(mx,my, cursor_size)

    for i in range(len(atoms)):
        atoms[i].display_atom()


### RENDERING PARTICLES END ###





### PHYSICS START ###
def contains(list, filter_x, filter_y, atomnumber):
    for x in list:
        if filter_x(x) and filter_y(x) and x != list[atomnumber]:
            return True
    return False


def Stacking(atom_A, atom_B):
    atom_A.y_velocity = 0
    atom_A.y_position -= 1
    Chemistry_Contact(atom_A, atom_B)

def sortx_position(self):
    return self.x_position

def sorty_position(self):
    return self.y_position





def Physics():
    global Temperature
    Average_Temperature = 0

    for i in range(len(atoms)):
        Average_Temperature += atoms[i].temperature


        if atoms[i].temperature < -273:
            atoms[i].temperature = -273

        if atoms[i].temperature < Temperature:
            atoms[i].temperature += 1/10*(Temperature - atoms[i].temperature)
        if atoms[i].temperature > Temperature:
            atoms[i].temperature += 1/10*(Temperature - atoms[i].temperature)

        if atoms[i].temperature > Atom_Dict[atoms[i].type]["Melting_temp"]:   #is melting
            atoms[i].state = "liquid"
        if atoms[i].temperature <= Atom_Dict[atoms[i].type]["Boiling_temp"]:   #is condensing
            atoms[i].state = "liquid"
        if atoms[i].temperature > Atom_Dict[atoms[i].type]["Boiling_temp"]:   #is boiling
            atoms[i].state = "gas"
        if atoms[i].temperature <= Atom_Dict[atoms[i].type]["Melting_temp"]:   #is freezing
            atoms[i].state = "solid"

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

        if atoms[i].state == "gas":
            atoms[i].x_velocity = atoms[i].x_velocity + (1/1)*random.randrange(-4, 4+1)
            atoms[i].y_velocity = atoms[i].y_velocity + (1/8)*random.randrange(-2, 2+1)

        if atoms[i].state == "liquid":
            atoms[i].y_velocity = atoms[i].y_velocity + (9.8 * 1/60)  # v = u + at
            atoms[i].x_velocity = atoms[i].x_velocity + (1/1)*random.randrange(-1, 1+1)
            atoms[i].y_velocity = atoms[i].y_velocity + (1/8)*random.randrange(-1, 1+1)

        if atoms[i].state == "solid":
            atoms[i].y_velocity = atoms[i].y_velocity + (9.8 * 1/60)  # v = u + at

        atoms[i].y_position = atoms[i].y_position + atoms[i].y_velocity
        atoms[i].x_position = atoms[i].x_position + atoms[i].x_velocity
        atoms[i].y_position = round(atoms[i].y_position)
        atoms[i].x_position = round(atoms[i].x_position)
        atoms[i].x_velocity = 0

        Coordinate_Holder = atoms[i].x_position, atoms[i].y_position
        coordinates.append(Coordinate_Holder)

    if len(atoms) != 0:
        if Temperature < Average_Temperature/len(atoms):
            Temperature -= 1/10*(Temperature - Average_Temperature/len(atoms))
        if Temperature > Average_Temperature/len(atoms):
            Temperature -= 1/10*(Temperature - Average_Temperature/len(atoms))

        #Temperature += 1/10*Average_Temperature/len(atoms)
        print(Average_Temperature/len(atoms))

    btoms = sorted(atoms, key=sortx_position)

    for i in range(len(atoms)):                     #Should check only when there is movement, and only on the particles that move
        if btoms[i].y_position == btoms[i-1].y_position and btoms[i].x_position == btoms[i-1].x_position and btoms[i] != btoms[i-1]:
            Stacking(btoms[i],btoms[i-1])
            btoms = sorted(atoms, key=sortx_position)


        if contains(atoms, lambda x: x.x_position == atoms[i].x_position, lambda x: x.y_position == atoms[i].y_position, i):
            Stacking(atoms[i],atoms[i-1])
            btoms = sorted(atoms, key=sortx_position)



### PHYSICS END ###






### CHEMISTRY START ###

def Chemistry_Contact(atom_1, atom_2):
    if atom_1.type in Reactant_1_list and atom_2.type in Reactant_2_list:
        if Reaction_Dict[atom_1.type]["Reactant_2"] == atom_2.type:
            Chemistry_Reaction(atom_1, atom_2)
    elif atom_2.type in Reactant_1_list and atom_1.type in Reactant_2_list:
        if Reaction_Dict[atom_2.type]["Reactant_2"] == atom_1.type:
            Chemistry_Reaction(atom_2, atom_1)


def Chemistry_Reaction(atom_1, atom_2):
    global Temperature
    global atom_delete_list
    global atom_create_list
    if Temperature >= Reaction_Dict[atom_1.type]["Temp_Required"]:
        Temperature += (1/10)*Reaction_Dict[atom_1.type]["Temp_Added"]
        if "+" in Reaction_Dict[atom_1.type]["Resultant"]:
            f = Reaction_Dict[atom_1.type]["Resultant"].split("+")
            atom_create_list.append([atom_1.x_position, atom_1.y_position, f[0], atom_1.x_velocity, atom_1.y_velocity])
            atom_create_list.append([atom_1.x_position, atom_1.y_position+1, f[1], atom_1.x_velocity, atom_1.y_velocity])
        else:
            atom_create_list.append([atom_1.x_position, atom_1.y_position, f[1], atom_1.x_velocity, atom_1.y_velocity])


        atom_delete_list.append(atom_1)
        atom_delete_list.append(atom_2)



### CHEMISTRY END ###



### SEPERATE PHYSICS LOOP FROM RENDERING ###


### LOADING ###

Atom_List = ["H", "He", "C", "N", "O", "Na", "Al", "Fe", "Au", "H2O", "FeO"]
Chemical_Information = LoadInformation("chemicalinfomation.txt")

Atom_Dict = {}
Chemical_Information_Other = LoadInformation("chemicalinfomation.txt")
Chemical_Information_Other.pop(0)
for i in Chemical_Information_Other:
    j = i.split("|")
    j_dict = {}
    j_dict["Melting_temp"] = float(j[5])
    j_dict["Boiling_temp"] = float(j[6])
    j_dict["Colour"] = int(j[8]),int(j[9]),int(j[10])
    Atom_Dict[j[1]] = j_dict

Reaction_Dict = {}
Reaction_Information = LoadInformation("chemicalreaction.txt")
Reaction_Information.pop(0)
for i in Reaction_Information:
    j = i.split("|")
    j_dict = {}
    j_dict["Reactant_1"] = j[0]
    j_dict["Reactant_1_Quantity"] = int(j[1])
    j_dict["Reactant_2"] = j[2]
    j_dict["Reactant_2_Quantity"] = int(j[3])
    j_dict["Resultant"] = j[4]
    j_dict["Resultant_Quantity"] = int(j[5])
    j_dict["Temp_Required"] = float(j[6])
    j_dict["Temp_Added"] = float(j[7])
    Reaction_Dict[j[0]] = j_dict

Reactant_1_list = []
Reactant_2_list = []
for i in Reaction_Dict:
    Reactant_1_list.append(i)
    Reactant_2_list.append(Reaction_Dict[i]["Reactant_2"])


coordinates = []

### MAIN LOOP ###

pygame.mouse.set_visible(False)
screen.fill((0,0,0))  # (R, G, B)



cursor_size = 4
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_c]:
                Selected_Molecule = input("THing: ")

    Atom_Manager() #Here because of threading



    #threads = []
    #Threading_Rendering_Particles = threading.Thread(target=Rendering_Particles)
    #threads.append(Threading_Rendering_Particles)
    #Threading_Rendering_Particles.start()

    #Threading_Physics = threading.Thread(target=Physics)
    #threads.append(Threading_Physics)
    #Threading_Physics.start()



    Rendering_Particles()
    Physics()



    ### CONSIDER LOCKING VARIABLES THAT ARE SHARED https://docs.python.org/3/library/threading.html#lock-objects and https://realpython.com/intro-to-python-threading/

    print("Temp: " + str(Temperature))
    pygame.display.update()
    clock.tick(60)
    end = perf_counter()
    FPS = (round(1/(end-start),2))
    print("FPS: " + str(FPS))
    start = perf_counter()
    print("PARTICLES: " + str(len(atoms)))

#pygame.quit()
