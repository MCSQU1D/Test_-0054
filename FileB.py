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
buttonsDict = {}
start = 0
end = 0
FPS = 300
FPS_List = [300,300,300,300,300]
cursor_size = 3
global InformationMenuToggleBool
InformationMenuToggleBool = False

Atom_List = ["H", "He", "C", "N", "O", "Na", "Al", "Fe", "Au", "H20"]


ButtonInformationDict = {
    "WorkSpace" : "Workspace: area for your reactions",
    "InformationPanel" : "Information Panel: Displays Information",
    "H" : "Hydrogen (H): A simple element, gas",
    "He" : "Helium (He): A simple element, gas",
    "C" : "Carbon (C): A nonmetal, powder",
    "N" : "Nitrogen (N): A simple element, gas",
    "O" : "Oxygen (O): A simple element, gas",
    "Ti" : "Titanium (Ti): A metal, powder",
    "Na" : "Sodium (Na): A alkali metal, powder",
    "Al" : "Aluminium (Al): A metal, powder",
    "Fe" : "Iron (Fe): A metal, powder",
    "Au" : "Gold (Au): A metal, powder",
    "H20" : "Water (H2O): A simple compound, liquid"
}


### FUNCTIONS ###

def MouseLocation():
    return pygame.mouse.get_pos()


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
    if file_finder == "chemicalinfomation.txt":
        file_pathname = os.getcwd()+"/files/chemicalinfomation.txt"  #finds the files folder
        file_opened = open(file_pathname,"r")
    file_split = file_opened.read().split("\n")
    return file_split

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
    if name not in ["InformationPanel", "WorkSpace"] and name != Selected_Molecule: #Only displays the name of the buttons on the sides
        PrintText((x1+x2)/2,(y1+y2)/2,name,'Apple II Pro.otf',12,(255, 255, 255))
    if name == Selected_Molecule:                                                   #if the button is the selected one, then it inverses the colour
        pygame.draw.rect(screen, (255,255,255), (x1+1,y1+1,x2-x1-2,y2-y1-2))        #White Background
        pygame.draw.rect(screen, (0,0,0), (x1,y1,x2-x1,y2-y1),1)                    #Black border
        PrintText((x1+x2)/2,(y1+y2)/2,name,'Apple II Pro.otf',12,(0, 0, 0))



def CreateCursor(x,y,size):
    pygame.draw.rect(screen, (255,255,255), (x-size/2,y-size/2,size,size),1)    #prints the square cursor

def InformationMenuToggle():
    global InformationMenuToggleBool
    if InformationMenuToggleBool == True:
        InformationMenuToggleBool = False
    elif InformationMenuToggleBool == False:
        InformationMenuToggleBool = True

def InformationMenu():
    global Information_Menu_Holder
    global InformationMenuToggleBool
    for i in Information_Menu_Holder:
        if i.split("|")[1] == Selected_Molecule:   #Uses symbol not name
            InformationMenu_List = i.split("|")
        elif Selected_Molecule not in i:
            InformationMenu_List = ["Select An Atom","N/A","N/A","N/A","N/A","N/A"]
    #InformationMenu_List = ["Title", "T", "0", "0", "Liquid", "debug tool"]
    if InformationMenuToggleBool == True:
        pygame.draw.rect(screen, (255,255,255), (260,30,390,450),1)    #prints the board for Information Menu, centred on 455
        pygame.draw.rect(screen, (255,255,255), (270,40,180,180),1)     #prints 180x180 square to contain images of atomic structure and natural state
        pygame.draw.rect(screen, (255,255,255), (460,40,180,180),1)
        pygame.draw.line(screen, (255,255,255), (270,250),(640,250),1) #Prints horizontal line for chemical name
        pygame.draw.line(screen, (255,255,255), (455,260),(455,340),1) #Prints vertical divider line

        PrintText(280+len("Chemical Symbol")*5.5,270,"Chemical Symbol",'Apple II Pro.otf',12,(255, 255, 255))
        PrintText(280+len("Atomic Number")*5.5,290,"Atomic Number",'Apple II Pro.otf',12,(255, 255, 255))
        PrintText(280+len("Atomic Mass")*5.5,310,"Atomic Mass",'Apple II Pro.otf',12,(255, 255, 255))
        PrintText(280+len("State at 20°C")*5.5,330,"State at 20°C",'Apple II Pro.otf',12,(255, 255, 255))
        PrintText(455,240,InformationMenu_List[0],'Apple II Pro.otf',18,(255, 255, 255))
        PrintText(280+len(InformationMenu_List[5])*5.5,360,InformationMenu_List[5],'Apple II Pro.otf',12,(255, 255, 255)) # the long text box at the bottom, needs algo for creating border and making it go down lines

        list = [InformationMenu_List[1],InformationMenu_List[2],InformationMenu_List[3],InformationMenu_List[4]]
        b = 250
        for j in list:
            b += 20
            PrintText(465+len(j)*5.5,(b),j,'Apple II Pro.otf',12,(255, 255, 255))  # broken and i don't know why





### LOADING ###
global Information_Menu_Holder
Information_Menu_Holder = LoadInformation("chemicalinfomation.txt")
#print(LoadInformation("chemicalinfomation.txt"))


### MAIN LOOP ###

running = True
while running == True:
    screen.fill((0,0,0))  # (R, G, B)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            #CreateButton(450,40,550,60,'yes?')
            if ButtonClick(MouseLocation()) not in ["WorkSpace", "InformationPanel", "Nil"]:
                #print(ButtonClick(MouseLocation()))
                Selected_Molecule = ButtonClick(MouseLocation())

        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_i]:
                InformationMenuToggle()

    InformationMenu()


    #print(ButtonHover(MouseLocation()))
    mx, my = pygame.mouse.get_pos()

    List_Shifter = 0
    for i in Atom_List:
        CreateButton(910,10+25*List_Shifter,950,30+25*List_Shifter, i)
        List_Shifter += 1

    CreateButton(10,10,900,500,'WorkSpace')
    CreateButton(10,510,900,530,'InformationPanel')
    PrintText(70, 25, "FPS: " + str(FPS), 'Apple II Pro.otf',12,(255, 255, 255))

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
        #pass


    pygame.mouse.set_visible(True)
    if ButtonHover(MouseLocation()) == "WorkSpace":
        pygame.mouse.set_visible(False)
        work_width, work_height = MouseLocation()
        work_height = 499 - work_height
        work_width -= 11
        PrintText(830, 25, "x:" + str(work_width) + " y:" + str(work_height), 'Apple II Pro.otf',12,(255, 255, 255))
        mx, my = MouseLocation()
        CreateCursor(mx,my,16)



    #pygame.draw.line(screen, (255,255,255), (480,270), (mx,my), 1)


    #print(MouseLocation())


    ButtonLocationPrintHolder = "Nil"
    # updates the display
    pygame.display.update()
    # clock.tick(framespersecond)
    clock.tick(60)
    end = perf_counter()
    FPS_List.pop(0)
    FPS_List.append(round(1/(end-start),1))
    FPS = 0
    for i in FPS_List:
        FPS += i
    FPS = round(FPS/5)
    start = perf_counter()

#pygame.quit()
