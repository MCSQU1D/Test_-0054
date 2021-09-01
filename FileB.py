import pygame
from time import sleep
from time import perf_counter
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

global Selected_Molecule
Selected_Molecule = "Nil"

ButtonLocationPrintHolder = "Nil"

global buttonsDict
global Temperature
global cursor_size
cursor_size = 4
global Physics_Running
Physics_Running = True
buttonsDict = {}
start = 0
end = 0
FPS = 300
Temperature = 20
FPS_List = [300,300,300,300,300]
global InformationMenuToggleBool
InformationMenuToggleBool = False

atoms = []
atomsRect = []

global atom_delete_list
atom_delete_list = []
global atom_create_list
atom_create_list = []

Atom_List = ["H", "He", "C", "N", "O", "Na", "Al", "Fe", "Au", "H2O", "FeO", "AlO"]
Element_List = ["H", "He", "C", "N", "O", "Na", "Al", "Fe", "Au"]
Compound_List = ["H2O", "FeO", "AlO"]


ButtonInformationDict = {
    "WorkSpace" : "Workspace: area for your reactions",
    "InformationPanel" : "Information Panel: Displays Information",
    "InformationMenu" : "Information Menu: Information on atoms",
    "Temp_Up" : "Increase temperature of Workspace, can use up arrow",
    "Temp_Down" : "Decrease temperature of Workspace, can use down arrow",
    "Clear_Atoms" : "Clear all atoms, can use 'c' key",
    "Physics_status" : "Plays/Pauses the particles movement, can use spacebar",
    "Info_status" : "Shows/hides Information menu, can use 'i' key",
    "H" : "Hydrogen (H): A simple element",
    "He" : "Helium (He): A simple element",
    "C" : "Carbon (C): A nonmetal",
    "N" : "Nitrogen (N): A simple element",
    "O" : "Oxygen (O): A simple element",
    "Na" : "Sodium (Na): A alkali metal",
    "Al" : "Aluminium (Al): A metal",
    "Fe" : "Iron (Fe): A metal",
    "Au" : "Gold (Au): A metal",
    "H2O" : "Water (H2O): A simple compound",
    "FeO" : "Iron Oxide (FeO): A simple compound",
    "AlO" : "Alumina (Al2O3): A simple compound"
}




### FUNCTIONS ###

def MouseLocation():
    return pygame.mouse.get_pos()

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
    file_pathname = os.getcwd()+"/files/" +file  #finds the files folder
    file_opened = open(file_pathname,"r")
    file_split = file_opened.read().split("\n")
    return file_split








### RENDERING SCREEN ###


def CreateCursor(x,y,size):
    pygame.draw.rect(screen, (255,255,255), (x-size/2-1,y-size/2-1,size+2,size+2),1)    #prints the square cursor



def PrintText(Xposition, Yposition, text, font, size, colour):
    global Selected_Molecule
    font = pygame.font.Font(font, size) #Font size
    LineHolder = text
    text = font.render(text, True, colour) #Font colour
    linewidth = text.get_width()
    textRect = text.get_rect()
    textRect.center = (Xposition, Yposition)
    screen.blit(text, textRect)


def ButtonClick(Mouse_Position):
    x, y = Mouse_Position
    #print(buttonsDict)
    ButtonLocationPrintHolder = "Nil"
    for ButtonLocations in buttonsDict:
        xlimithigh = ButtonLocations[0]
        xlimitlow = ButtonLocations[1]
        ylimithigh = ButtonLocations[2]
        ylimitlow = ButtonLocations[3]

        if x > xlimithigh and x < xlimitlow and y > ylimithigh and y < ylimitlow:
            ButtonLocationPrintHolder = buttonsDict[ButtonLocations]
    return ButtonLocationPrintHolder


def LoadImage(file):
    path = os.path.join("files")
    filelist = []
    for r, d, f in os.walk(path):
        for file_finder in f:
            if '.jpg' in file_finder:
                filelist.append(file_finder)
    for i in filelist:
        if file in i:
            return pygame.image.load(os.path.join('files', i))
    return pygame.image.load(os.path.join('files', ("No_Image_Found.jpg")))

def ButtonHover(Mouse_Position):
    x, y = Mouse_Position
    #print(buttonsDict)
    ButtonLocationPrintHolder = "Nil"
    for ButtonLocations in buttonsDict:
        xlimithigh = ButtonLocations[0]
        xlimitlow = ButtonLocations[1]
        ylimithigh = ButtonLocations[2]
        ylimitlow = ButtonLocations[3]

        if x > xlimithigh and x < xlimitlow and y > ylimithigh and y < ylimitlow:
            ButtonLocationPrintHolder = buttonsDict[ButtonLocations]
    return ButtonLocationPrintHolder


def CreateButton(x1,y1,x2,y2,name):
    global Selected_Molecule
    buttonsDict[(x1, x2, y1, y2)] = name                                            #Sets the name for the button in the button dictionary
    pygame.draw.rect(screen, (255,255,255), (x1,y1,x2-x1,y2-y1),1)                  #Draws the button boundary
    if name not in ["InformationPanel", "WorkSpace", "InformationMenu", "Temp_Up", "Temp_Down", "Clear_Atoms", "Physics_status", "Info_status"] and name != Selected_Molecule: #Only displays the name of the buttons on the sides
        PrintText((x1+x2)/2,(y1+y2)/2,name,'Apple II Pro.otf',12,(255, 255, 255))
    if name == "Temp_Up":
        PrintText((x1+x2)/2,(y1+y2)/2,"↑",'Apple II Pro.otf',12,(255, 255, 255))
    if name == "Temp_Down":
        PrintText((x1+x2)/2,(y1+y2)/2,"↓",'Apple II Pro.otf',12,(255, 255, 255))
    if name == "Clear_Atoms":
        PrintText((x1+x2)/2,(y1+y2)/2,"CLR",'Apple II Pro.otf',12,(255, 255, 255))
    if name == "Physics_status":
        if Physics_Running == True:
            PrintText((x1+x2)/2,(y1+y2)/2,"PLY",'Apple II Pro.otf',12,(255, 255, 255))
        if Physics_Running == False:
            pygame.draw.rect(screen, (255, 255, 255), (x1+1,y1+1,x2-x1-2,y2-y1-2))
            pygame.draw.rect(screen, (0,0,0), (x1,y1,x2-x1,y2-y1),1)
            PrintText((x1+x2)/2,(y1+y2)/2,"PSE",'Apple II Pro.otf',12,(0, 0, 0))
    if name == "Info_status":
        if InformationMenuToggleBool == False:
            PrintText((x1+x2)/2,(y1+y2)/2,"INF",'Apple II Pro.otf',12,(255, 255, 255))
        if InformationMenuToggleBool == True:
            pygame.draw.rect(screen, (255, 255, 255), (x1+1,y1+1,x2-x1-2,y2-y1-2))
            pygame.draw.rect(screen, (0,0,0), (x1,y1,x2-x1,y2-y1),1)
            PrintText((x1+x2)/2,(y1+y2)/2,"INF",'Apple II Pro.otf',12,(0, 0, 0))
    if name == Selected_Molecule:                                                   #if the button is the selected one, then it inverses the colour
        pygame.draw.rect(screen, Atom_Dict[Selected_Molecule]["Colour"], (x1+1,y1+1,x2-x1-2,y2-y1-2))        #White Background
        pygame.draw.rect(screen, (0,0,0), (x1,y1,x2-x1,y2-y1),1)                    #Black border
        PrintText((x1+x2)/2,(y1+y2)/2,name,'Apple II Pro.otf',12,(0, 0, 0))



def InformationMenuToggle():
    global InformationMenuToggleBool
    if InformationMenuToggleBool == True:
        InformationMenuToggleBool = False
        del buttonsDict[(20,220,40,490)]
    elif InformationMenuToggleBool == False:
        InformationMenuToggleBool = True

def InformationMenu():
    global Information_Menu_Holder
    global InformationMenuToggleBool
    for i in Information_Menu_Holder:
        if i.split("|")[1] == Selected_Molecule:   #Uses symbol not name
            InformationMenu_List = i.split("|")
            break                                   #Fixed the problem where this would then go on to the elif statement <- is bad
        if Selected_Molecule in ButtonInformationDict:
            InformationMenu_List = ["Compound",Selected_Molecule,"N/A","N/A","Unknown","It is a random compound"]
        else:
            InformationMenu_List = ["Select an Atom","N/A","N/A","N/A","N/A","N/A"]
    #InformationMenu_List = ["Title", "T", "0", "0", "Liquid", "debug tool"]
    if InformationMenuToggleBool == True:
        pygame.draw.rect(screen, (0,0,0), (20,40,200,450),0)
        CreateButton(20,40,220,490,"InformationMenu")                   #prints the board for Information Menu, offset from center

        if InformationMenu_List[1] in Element_List:
            pygame.draw.rect(screen, (255,255,255), (30,50,180,180),1)      #prints 180x180 square to contain images of atomic structure
            pygame.draw.line(screen, (255,255,255), (30,255),(210,255),1)   #Prints horizontal line for chemical name
            pygame.draw.line(screen, (255,255,255), (155,260),(155,380),1)  #Prints vertical divider line
            list = [InformationMenu_List[1],InformationMenu_List[2],InformationMenu_List[3],InformationMenu_List[4],InformationMenu_List[5]+"°C",InformationMenu_List[6]+"°C"]
            Paragrapher(InformationMenu_List[7],95,10,30+len(InformationMenu_List[5])*4.5,390) # the long text box at the bottom, needs algo for creating border and making it go down lines
            screen.blit(LoadImage(InformationMenu_List[0]), (30, 50))

            PrintText(120,245,InformationMenu_List[0],'Apple II Pro.otf',14,(255, 255, 255))
            PrintText(30+len("Symbol")*4.5,270,"Symbol",'Apple II Pro.otf',10,(255, 255, 255))
            PrintText(30+len("Atomic Number")*4.5,290,"Atomic Number",'Apple II Pro.otf',10,(255, 255, 255))
            PrintText(30+len("Mass (u)")*4.5,310,"Mass (u)",'Apple II Pro.otf',10,(255, 255, 255))
            PrintText(30+len("State at 20°C")*4.5,330,"State at 20°C",'Apple II Pro.otf',10,(255, 255, 255))
            PrintText(30+len("Melting Temp")*4.5,350,"Melting Temp",'Apple II Pro.otf',10,(255, 255, 255))
            PrintText(30+len("Boiling Temp")*4.5,370,"Boiling Temp",'Apple II Pro.otf',10,(255, 255, 255))


        elif InformationMenu_List[1] in Compound_List:
            pygame.draw.rect(screen, (255,255,255), (30,50,180,180),1)      #prints 180x180 square to contain images of atomic structure
            pygame.draw.line(screen, (255,255,255), (30,255),(210,255),1)   #Prints horizontal line for chemical name
            pygame.draw.line(screen, (255,255,255), (155,260),(155,380),1)  #Prints vertical divider line
            list = [InformationMenu_List[1],InformationMenu_List[2],InformationMenu_List[3],InformationMenu_List[4],InformationMenu_List[5]+"°C",InformationMenu_List[6]+"°C"]
            Paragrapher(InformationMenu_List[7],95,10,30+len(InformationMenu_List[5])*4.5,390) # the long text box at the bottom, needs algo for creating border and making it go down lines
            screen.blit(LoadImage(InformationMenu_List[0]), (30, 50))

            PrintText(120,245,InformationMenu_List[0],'Apple II Pro.otf',14,(255, 255, 255))
            PrintText(30+len("Formula")*4.5,270,"Formula",'Apple II Pro.otf',10,(255, 255, 255))
            PrintText(30+len("Mass (g/mol)")*4.5,310,"Mass (g/mol)",'Apple II Pro.otf',10,(255, 255, 255))
            PrintText(30+len("Composition")*4.5,290,"Composition",'Apple II Pro.otf',10,(255, 255, 255))
            PrintText(30+len("State at 20°C")*4.5,330,"State at 20°C",'Apple II Pro.otf',10,(255, 255, 255))
            PrintText(30+len("Melting Temp")*4.5,350,"Melting Temp",'Apple II Pro.otf',10,(255, 255, 255))
            PrintText(30+len("Boiling Temp")*4.5,370,"Boiling Temp",'Apple II Pro.otf',10,(255, 255, 255))

        else:
            list = ["","","","","",""]
            text = "On the right hand       that side ==>    you will find buttons to press to select an atom, then this menu will display that information for you."
            Paragrapher(text,95,10,30+len(InformationMenu_List[5])*4.5,60) # the long text box at the bottom, needs algo for creating border and making it go down lines

        b = 250
        for j in list:
            b += 20
            PrintText(160+len(j)*4.5,(b),j,'Apple II Pro.otf',10,(255, 255, 255))  # broken and i don't know why - fixed

def Paragrapher(string,length,fontsize,xposition,yposition):
    TextSplit = string.split(' ')
    TextHolder = ""
    TextFinal = []
    for i in TextSplit:
        if len(TextHolder + " " + i)*(45/fontsize) >= length:
            TextFinal.append(TextHolder)
            TextHolder = ""
        if len(TextHolder + " " + i)*(45/fontsize) < length and i != TextSplit[-1]:
            TextHolder = TextHolder + " " + i
        else:
            TextHolder = TextHolder + " " + i
            TextFinal.append(TextHolder)
            TextHolder = ""
    for text in TextFinal:
        PrintText(20+len(text)*4.5,yposition, text,'Apple II Pro.otf',fontsize,(255, 255, 255))
        yposition += 12

def ScreenMagic():       #Changes the mouse
    global cursor_size
    screen.fill((0,0,0))  # (R, G, B)
    pygame.mouse.set_visible(True)
    if ButtonHover(MouseLocation()) == "WorkSpace":
        pygame.mouse.set_visible(False)
        work_width, work_height = MouseLocation()
        work_height = 499 - work_height
        work_width -= 11
        PrintText(830, 25, "x:" + str(work_width) + " y:" + str(work_height), 'Apple II Pro.otf',12,(255, 255, 255))
        mx, my = MouseLocation()
        CreateCursor(mx,my, cursor_size)
    pygame.draw.rect(screen, (0,0,0), (0,0,10,500),0)
    pygame.draw.rect(screen, (0,0,0), (0,500,960,540),0)
    pygame.draw.rect(screen, (0,0,0), (900,0,960,540),0)
    pygame.draw.rect(screen, (0,0,0), (0,0,960,10),0)



def Rendering_BaseScreen():
    InformationMenu()
    mx, my = pygame.mouse.get_pos()
    List_Shifter = 0
    for i in Atom_List:
        CreateButton(910,10+25*List_Shifter,950,30+25*List_Shifter, i)
        List_Shifter += 1

    CreateButton(10,10,900,500,'WorkSpace')
    CreateButton(10,510,900,530,'InformationPanel')
    PrintText(70, 25, "FPS: " + str(FPS), 'Apple II Pro.otf',12,(255, 255, 255))
    PrintText(240, 25, "Particles: " + str(len(atoms)), 'Apple II Pro.otf',12,(255, 255, 255))
    PrintText(455, 25, "Temp: " + str(int(Temperature)) + "°C (" + str(int(Temperature*9/5+32)) + "°F)", 'Apple II Pro.otf',12,(255, 255, 255))
    if ButtonHover(MouseLocation()) != "Nil":
        name = ButtonInformationDict[ButtonHover(MouseLocation())]
        x1 = 10
        x2 = 900
        y1 = 510
        y2 = 530
        PrintText((x1+x2)/2,(y1+y2)/2,name,'Apple II Pro.otf',12,(255, 255, 255))
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    if ButtonHover(MouseLocation()) in Atom_List:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)






def BaseScreen_Adjustment():
    pygame.draw.line(screen, (255,255,255), (10,10), (899,10), 1)
    pygame.draw.line(screen, (255,255,255), (899,10), (899,499), 1)
    pygame.draw.line(screen, (255,255,255), (899,499), (10,499), 1)
    pygame.draw.line(screen, (255,255,255), (10,499), (10,10), 1)
    #pass


### RENDERING SCREEN END ###















### PARTICLES START ###

class atom:
    def __init__(self, x_position, y_position, type):
        self.x_position = x_position
        self.y_position = y_position
        self.type = type
        self.x_velocity = 0
        self.y_velocity = 0
        self.colour = Atom_Dict[type]["Colour"]
        self.temperature = Temperature
        self.state = "solid"



    def display_atom(self):
        pass
        rect = pygame.Rect(self.x_position, self.y_position, 1, 1)
        pygame.draw.rect(screen, (self.colour), rect)


def SimulatorMousePressedAdd(size):
    if Selected_Molecule != "Nil":
        mx,my = pygame.mouse.get_pos()
        for i in range(-round(size/2)-1,round(size/2)+1):
            for j in range(-round(size/2)-1,round(size/2)+1):
                if mx+i < 900 and mx+i > 10 and my+j > 10 and my+j < 500:
                    atoms.append(atom(mx+i, my+j, Selected_Molecule))


def SimulatorMousePressedRemove(size):
    mx,my = pygame.mouse.get_pos()
    atomdeletelist=[]
    for i in range(len(atoms)):
        if atoms[i].x_position >= mx-round(cursor_size/2)-1 and atoms[i].x_position <= mx+round(cursor_size/2) and atoms[i].y_position >= my-round(cursor_size/2)-1 and atoms[i].y_position <= my+round(cursor_size/2):
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

    for j in atom_create_list:
        atoms.append(atom(j[0], j[1], j[2]))
        atoms[-1].x_velocity = j[3]
        atoms[-1].x_velocity = j[4]
    atom_create_list = []


def Rendering_Particles():

    if pygame.mouse.get_pressed()[0] == 1:
        SimulatorMousePressedAdd(cursor_size)
        #pass

    if pygame.mouse.get_pressed()[2] == 1:
        SimulatorMousePressedRemove(cursor_size)

    mx,my = pygame.mouse.get_pos()

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
        if atoms[i].x_position > 898:
            atoms[i].x_position = 898
            atoms[i].x_velocity = 0

        if atoms[i].x_position < 12:
            atoms[i].x_position = 12
            atoms[i].x_velocity = 0

        if atoms[i].y_position > 498:
             atoms[i].y_position = 498
             atoms[i].y_velocity = 0

        if atoms[i].y_position < 12:
            atoms[i].y_position = 12
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
            for o in f:
                atom_create_list.append([atom_1.x_position, atom_1.y_position+1, o, atom_1.x_velocity, atom_1.y_velocity])
        else:
            atom_create_list.append([atom_1.x_position, atom_1.y_position, Reaction_Dict[atom_1.type]["Resultant"], atom_1.x_velocity, atom_1.y_velocity])


        atom_delete_list.append(atom_1)
        atom_delete_list.append(atom_2)

### CHEMISTRY END ###



def Screen_Controls():
    CreateButton(910,480,950,500,'Temp_Up')
    CreateButton(910,510,950,530,'Temp_Down')
    CreateButton(910,450,950,470,'Clear_Atoms')
    CreateButton(910,420,950,440,'Physics_status')
    CreateButton(910,390,950,410,'Info_status')
    global Temperature
    if pygame.key.get_pressed()[pygame.K_UP] == True:
        Temperature += 1
    if pygame.key.get_pressed()[pygame.K_UP] == True and pygame.key.get_pressed()[pygame.K_LSHIFT] == True:
        Temperature += 100
    if pygame.key.get_pressed()[pygame.K_DOWN] == True:
        Temperature -= 1
    if pygame.key.get_pressed()[pygame.K_DOWN] == True and pygame.key.get_pressed()[pygame.K_LSHIFT] == True:
        Temperature -= 100
    if Temperature < -273:
        Temperature = -273










### LOADING ###




global Information_Menu_Holder
Information_Menu_Holder = LoadInformation("chemicalinfomation.txt")


Chemical_Information_Other = LoadInformation("chemicalinfomation.txt")
Chemical_Information_Other.pop(0)
Atom_Dict = {}
for i in Chemical_Information_Other:
    j = i.split("|")
    j_dict = {}
    j_dict["Melting_temp"] = float(j[5])
    j_dict["Boiling_temp"] = float(j[6])
    j_dict["Colour"] = int(j[8]),int(j[9]),int(j[10])

    Atom_Dict[j[1]] = j_dict

Atom_List = ["H", "He", "C", "N", "O", "Na", "Al", "Fe", "Au", "H2O", "FeO", "AlO"]
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





### END LOADING ###



### MAIN LOOP ###


running = True
while running == True:
    ScreenMagic()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #CreateButton(450,40,550,60,'yes?')
            if ButtonClick(MouseLocation()) not in ["WorkSpace", "InformationPanel", "InformationMenu", "Temp_Up", "Temp_Down", "Clear_Atoms", "Physics_status", "Info_status", "Nil"]:
                #print(ButtonClick(MouseLocation()))
                Selected_Molecule = ButtonClick(MouseLocation())
            if ButtonClick(MouseLocation()) == "Temp_Up":
                Temperature += 1
            if ButtonClick(MouseLocation()) == "Temp_Down":
                Temperature -= 1
            if ButtonClick(MouseLocation()) == "Physics_status":
                if Physics_Running == True:
                    Physics_Running = False
                elif Physics_Running == False:
                    Physics_Running = True
            if ButtonClick(MouseLocation()) == "Info_status":
                if InformationMenuToggleBool == True:
                    InformationMenuToggleBool = False
                elif InformationMenuToggleBool == False:
                    InformationMenuToggleBool = True
            if ButtonClick(MouseLocation()) == "Clear_Atoms":
                for i in atoms:
                    atom_delete_list.append(i)
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_i]:
                InformationMenuToggle()
            if key[pygame.K_c]:
                for i in atoms:
                    atom_delete_list.append(i)
            if key[pygame.K_SPACE]:
                if Physics_Running == True:
                    Physics_Running = False
                elif Physics_Running == False:
                    Physics_Running = True


    Rendering_BaseScreen()

    Atom_Manager()


    Rendering_Particles()

    if Physics_Running == True:
        Physics()


    BaseScreen_Adjustment()




    Screen_Controls()
    ButtonLocationPrintHolder = "Nil"
    pygame.display.update()

    clock.tick(60)
    end = perf_counter()
    FPS_List.pop(0)
    FPS_List.append(round(1/(end-start),1))
    FPS = 0
    for i in FPS_List:
        FPS += i
    FPS = round(FPS/5)
    start = perf_counter()
