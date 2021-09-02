import pygame
import random
import os


pygame.init()
Ratios = [0.25, 1/3, 0.5, 2/3, 0.75, 5/6, 1]
size_ratio = Ratios[2]


display_width = int(1920*size_ratio)
display_height = int(1080*size_ratio)
Legal_Toggle = False

# initialize the pygame module



### SREEN, CLOCK AND DISPLAY ###
screen = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
pygame.display.set_caption("TEST: #0054")

screen.fill((0,0,0))  # (R, G, B)
#background_image = pygame.image.load('background_02.png')
#screen.blit(background_image, (0, 0))




global buttonsDict
buttonsDict = {

}



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

    file_pathname = os.getcwd()+"/files/" +file
    file_opened = open(file_pathname,"r")
    file_split = file_opened.read().split("\n")
    return file_split


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
        PrintText(30+len(text)*4.5,yposition, text,'Apple II Pro.otf',fontsize,(255, 255, 255))
        yposition += 12

def PrintLegal():
    pygame.draw.rect(screen, (0,0,0), (0,0,1*display_width,25*display_height/27))
    PrintText((display_width/2), (4*display_height/27), "Legal Information and Disclaimer", 'Apple II ALT Pro.otf', int(60*size_ratio), (255,255,255))
    Paragrapher(LoadInformation("legal.txt")[0],450,10,50,6*display_height/27)



def CreateButton(x1,y1,x2,y2,name):
    buttonsDict[(x1, x2, y1, y2)] = name
    #pygame.draw.rect(screen, (255,255,255), (x1,y1,x2-x1,y2-y1))
    #pygame.draw.rect(screen, (0,0,0), (x1+1,y1+1,x2-x1-2,y2-y1-2))
    #PrintText((x1+x2)/2,(y1+y2)/2,name,'Apple II Pro.otf',12,(255,255,255))


funny_comment_list = LoadInformation("funny.txt")
funny_comment = funny_comment_list[random.randint(0, len(funny_comment_list)-1)]

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
            if ButtonClick(MouseLocation()) == "Legal":
                if Legal_Toggle == True:
                    Legal_Toggle = False
                    screen.fill((0,0,0))
                elif Legal_Toggle == False:
                    Legal_Toggle = True



    PrintText((display_width/2), (8*display_height/30), funny_comment, 'Apple II Pro.otf', int(24*size_ratio), (255,0,0))
    PrintText((display_width/2), (5*display_height/27), "TEST:#0054", 'Apple II ALT Pro.otf', int(140*size_ratio), (255,255,255))
    PrintText((display_width/2), (15*display_height/27), "BEGIN", 'Apple II ALT Pro.otf', int(110*size_ratio), (255,255,255))
    PrintText((display_width/2), (20*display_height/27), "QUIT", 'Apple II ALT Pro.otf', int(110*size_ratio), (255,255,255))
    PrintText((5*display_width/6), (26*display_height/27), "Developed by Samuel McKid", 'Apple II Pro.otf', int(24*size_ratio), (255,0,0))
    PrintText((1*display_width/16), (26*display_height/27), "Legal", 'Apple II Pro.otf', int(24*size_ratio), (255,0,0))

    CreateButton(6*display_width/16,13*display_height/27,10*display_width/16,17*display_height/27,'Begin')
    CreateButton(3*display_width/8,2*display_height/3,5*display_width/8,22*display_height/27,'Quit')
    CreateButton(0*display_width,25*display_height/27,1*display_width/8,1*display_height,'Legal')

    if Legal_Toggle == True:
        PrintLegal()

    #Printer_1 = 0
    #for i in Ratios:
        #Ratio_Printer = (str(int(1920*i)) + "x" + str(int(1080*i)))
        #CreateButton((0),(7*display_height/27 + 2*display_height/27*Printer_1),(2*display_width/16),(9*display_height/27 + 2*display_height/27*Printer_1), Printer_1) #ADJUST BUTTTON AREAs
        #PrintText((display_width/16), (8*display_height/27 + 2*display_height/27*Printer_1), Ratio_Printer, 'Apple II Pro.otf', int(28*size_ratio), (255,255,255))
        #Printer_1 += 1

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
