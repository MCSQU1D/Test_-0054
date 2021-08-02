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

screen.fill((0,0,0))  # (R, G, B)
#background_image = pygame.image.load('background_01.png')
#screen.blit(background_image, (0, 0))


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
            print(ButtonClick(MouseLocation()))
            #if ButtonClick(MouseLocation()) == "Quit":
            #    running = False

            #if ButtonClick(MouseLocation()) == "Begin":
            #    running = False
            #    import FileB
        #if event.type == pygame.TEXTINPUT:
            #print(pygame.KEYDOWN)

    #print()


    #screen.blit(background_image, (0, 0))

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
