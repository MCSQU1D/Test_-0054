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

global Selected_Molecule
Selected_Molecule = "Nil"

ButtonLocationPrintHolder = "Nil"

global buttonsDict
buttonsDict = {

}

List = ["H", "He", "C", "N", "O", "Ti", "Fe", "Au", "H20"]

ButtonInformationDict = {
    "WorkSpace" : "Workspace: area for your reactions",
    "InformationPanel" : "Information Panel: Displays Information",
    "H" : "Hydrogen (H): A simple element, gas",
    "He" : "Helium (He): A simple element, gas",
    "C" : "Carbon (C): A simple element, powder",
    "N" : "Nitrogen (N): A simple element, gas",
    "O" : "Oxygen (O): A simple element, gas",
    "Ti" : "Titanium (Ti): A metal, powder",
    "Fe" : "Iron (Fe): A metal, powder",
    "Au" : "Gold (Au): A metal, powder",
    "H20" : "Water (H2O): A simple compound, liquid"
}


### FUNCTIONS ###

def MouseLocation():
    return pygame.mouse.get_pos()


def PrintText(Xposition, Yposition, text, font, size):
    global Selected_Molecule
    font = pygame.font.Font(font, size) #Font size
    LineHolder = text
    if text == Selected_Molecule:
        text = font.render(text, True, (0, 0, 0)) #Font colour
    else:
        text = font.render(text, True, (255, 255, 255)) #Font colour
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
    buttonsDict[(x1, x2, y1, y2)] = name
    pygame.draw.rect(screen, (255,255,255), (x1,y1,x2-x1,y2-y1))
    pygame.draw.rect(screen, (0,0,0), (x1+1,y1+1,x2-x1-2,y2-y1-2))
    if name == Selected_Molecule:
        pygame.draw.rect(screen, (0,0,0), (x1,y1,x2-x1,y2-y1))
        pygame.draw.rect(screen, (255,255,255), (x1+1,y1+1,x2-x1-2,y2-y1-2))
    if name not in ["InformationPanel", "WorkSpace"]:
        PrintText((x1+x2)/2,(y1+y2)/2,name,'Apple II Pro.otf',12)






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
                print(ButtonClick(MouseLocation()))
                Selected_Molecule = ButtonClick(MouseLocation())

    #print(ButtonHover(MouseLocation()))
    mx, my = pygame.mouse.get_pos()


    List_Shifter = 0
    for i in List:
        CreateButton(910,10+25*List_Shifter,950,30+25*List_Shifter, i)
        List_Shifter += 1

    CreateButton(10,10,900,500,'WorkSpace')
    CreateButton(10,510,900,530,'InformationPanel')
    if ButtonHover(MouseLocation()) != "Nil":
        name = ButtonInformationDict[ButtonHover(MouseLocation())]
        x1 = 10
        x2 = 900
        y1 = 510
        y2 = 530
        PrintText((x1+x2)/2,(y1+y2)/2,name,'Apple II Pro.otf',12)


    if ButtonHover(MouseLocation()) == "WorkSpace":
        work_width, work_height = MouseLocation()
        work_height = 499 - work_height
        work_width -= 11
        PrintText(830, 25, "x:" + str(work_width) + " y:" + str(work_height), 'Apple II Pro.otf',12)


    #PrintText(mx, my, "I", 'ArchitectsDaughter-Regular.ttf', 120)
    #pygame.draw.line(screen, (255,255,255), (480,270), (mx,my), 1)


    #print(MouseLocation())


    ButtonLocationPrintHolder = "Nil"
    # updates the display
    pygame.display.update()
    # clock.tick(framespersecond)
    clock.tick(60)

#pygame.quit()
