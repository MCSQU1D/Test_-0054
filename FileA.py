import pygame
from time import sleep
import random
import os
import math
from multiprocessing import Process


pygame.init()
Ratios = [0.25, 1/3, 0.5, 2/3, 0.75, 5/6, 1]
size_ratio = Ratios[2]

display_width = int(1920*size_ratio)
display_height = int(1080*size_ratio)


# initialize the pygame module



### SREEN, CLOCK AND DISPLAY ###
screen = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
pygame.display.set_caption("TEST: #0054")

#screen.fill((255,255,255))  # (R, G, B)
background_image = pygame.image.load('background_01.png')
screen.blit(background_image, (0, 0))


global buttonsDict
buttonsDict = {

}



def MouseLocation():
    return pygame.mouse.get_pos()


def PrintText(Xposition, Yposition, text, font, size, colour):
    font = pygame.font.Font(font, size) #Font size
    LineHolder = text
    text = font.render(text, True, colour) #Font colour
    linewidth = text.get_width()
    textRect = text.get_rect()
    textRect.center = (Xposition, Yposition)
    screen.blit(text, textRect)


def ButtonClick(Mouse_Position):
    ButtonLocationPrintHolder = "nil"
    x, y = Mouse_Position
    #print(buttonsDict)
    for ButtonLocations in buttonsDict:
        xlimithigh = ButtonLocations[0]
        xlimitlow = ButtonLocations[1]
        ylimithigh = ButtonLocations[2]
        ylimitlow = ButtonLocations[3]
        #print(ButtonLocations)

        if x > xlimithigh and x < xlimitlow and y > ylimithigh and y < ylimitlow:
            ButtonLocationPrintHolder = buttonsDict[ButtonLocations]
            #print(ButtonLocationPrintHolder)
    return ButtonLocationPrintHolder


def CreateButton(x1,y1,x2,y2,name):
    buttonsDict[(x1, x2, y1, y2)] = name
    #pygame.draw.rect(screen, (255,255,255), (x1,y1,x2-x1,y2-y1))
    #pygame.draw.rect(screen, (0,0,0), (x1+1,y1+1,x2-x1-2,y2-y1-2))
    #PrintText((x1+x2)/2,(y1+y2)/2,name,'Apple II Pro.otf',12)

# main loop
running = True
while running == True:
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            #print(ButtonClick(MouseLocation()))
            if ButtonClick(MouseLocation()) == "Quit":
                running = False

            if ButtonClick(MouseLocation()) == "Begin":
                running = False
                import FileB
            if ButtonClick(MouseLocation()) in [0,1,2,3,4,5,6,7]:
                print(Ratios[ButtonClick(MouseLocation())])
                size_ratio = Ratios[ButtonClick(MouseLocation())]
                display_width = int(1920*size_ratio)
                display_height = int(1080*size_ratio)



    screen.blit(background_image, (0, 0))
    PrintText((display_width/2), (5*display_height/27), "TEST: #0054", 'ArchitectsDaughter-Regular.ttf', int(240*size_ratio), (255,255,255))
    PrintText((display_width/2), (15*display_height/27), "BEGIN", 'ArchitectsDaughter-Regular.ttf', int(160*size_ratio), (255,255,255))
    PrintText((display_width/2), (20*display_height/27), "QUIT", 'ArchitectsDaughter-Regular.ttf', int(160*size_ratio), (255,255,255))
    PrintText((43*display_width/48), (26*display_height/27), "Developed by Samuel McKid", 'ArchitectsDaughter-Regular.ttf', int(24*size_ratio), (255,255,255))

    CreateButton(3*display_width/8,13*display_height/27,5*display_width/8,17*display_height/27,'Begin')
    CreateButton(3*display_width/8,2*display_height/3,5*display_width/8,22*display_height/27,'Quit')

    Printer_1 = 0
    for i in Ratios:
        Ratio_Printer = (str(int(1920*i)) + "x" + str(int(1080*i)))
        CreateButton((0),(7*display_height/27 + 2*display_height/27*Printer_1),(2*display_width/16),(9*display_height/27 + 2*display_height/27*Printer_1), Printer_1) #ADJUST BUTTTON AREAs
        PrintText((display_width/16), (8*display_height/27 + 2*display_height/27*Printer_1), Ratio_Printer, 'ArchitectsDaughter-Regular.ttf', int(48*size_ratio), (255,255,255))
        Printer_1 += 1

    #reset button print variable
    ButtonLocationPrintHolder = 'Nil'
    # updates the display
    pygame.display.update()
    # clock.tick(framespersecond)
    #buttonsDict.clear()
    #resets screen size if there is a change
    display_width = int(1920*size_ratio)
    display_height = int(1080*size_ratio)
    screen = pygame.display.set_mode((display_width,display_height))
    clock.tick(60)



pygame.quit()
