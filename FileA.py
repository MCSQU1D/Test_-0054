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
screen = pygame.display.set_mode((display_width,display_height))    # sets time, creates display, logos and caption
clock = pygame.time.Clock()
pygame.display.set_caption("TEST: #0054")
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)

screen.fill((0,0,0))  # (R, G, B), fills the screen, black
#background_image = pygame.image.load('background_02.png')
#screen.blit(background_image, (0, 0))




global buttonsDict
buttonsDict = {

}








### VERY IMPORTANT SORT ALGORITHM THAT DOES ALOT START ###
global UnsortedList
global UnsortedListb
UnsortedList = []
for i in range(100):
    UnsortedList.append(random.randrange(0, 100))
UnsortedListb = UnsortedList

def theNumbers():
    global UnsortedList
    Numitems = len(UnsortedList)
    CurrentItem = 1
    #UnsortedList.sort()
    while CurrentItem <= Numitems - 1:
        CurrentDataItem = UnsortedList[CurrentItem]
        Comparison = 0
        Finish = False
        while Comparison < CurrentItem and Finish == False:
            if CurrentDataItem < UnsortedList[Comparison]:
                ShuffleItem = CurrentItem
                while ShuffleItem > Comparison:
                    UnsortedList[ShuffleItem] = UnsortedList[ShuffleItem-1]
                    ShuffleItem = ShuffleItem - 1
                UnsortedList[Comparison] = CurrentDataItem
                Finish = True
            Comparison += 1
        CurrentItem += 1
    return(UnsortedList)
### VERY IMPORTANT SORT ALGORITHM THAT DOES ALOT END ###

#print(theNumbers())









def MouseLocation():
    return pygame.mouse.get_pos()  #gets mouse sise in simple and easy manner


def LoadInformation(file):     #gets .txt files, splits into list of each lines
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


def PrintText(Xposition, Yposition, text, font, size, colour):   #prints text on screen
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
    for ButtonLocations in buttonsDict:    #stores all buttons as a dictionary, where the button is defined by the its borders
        xlimithigh = ButtonLocations[0]
        xlimitlow = ButtonLocations[1]
        ylimithigh = ButtonLocations[2]
        ylimitlow = ButtonLocations[3]
        #print(ButtonLocations)

        if x > xlimithigh and x < xlimitlow and y > ylimithigh and y < ylimitlow:
            ButtonLocationPrintHolder = buttonsDict[ButtonLocations]
            #print(ButtonLocationPrintHolder)
    return ButtonLocationPrintHolder

def Paragrapher(string,length,fontsize,xposition,yposition):            # takes a string a splits it into a paragraph (i.e. inserts enters after a certain length)
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

def PrintLegal():          #prints legal information page (over the top of other page)
    pygame.draw.rect(screen, (0,0,0), (0,0,1*display_width,25*display_height/27))
    PrintText((display_width/2), (4*display_height/27), "Legal Information and Disclaimer", 'Apple II ALT Pro.otf', int(60*size_ratio), (255,255,255))
    Paragrapher(LoadInformation("legal.txt")[0],450,10,50,6*display_height/27)



def CreateButton(x1,y1,x2,y2,name):             #create the button by the name defined by the limits
    buttonsDict[(x1, x2, y1, y2)] = name


funny_comment_list = LoadInformation("funny.txt")
funny_comment = funny_comment_list[random.randint(0, len(funny_comment_list)-1)]        #randomly picks a funny comment from the .txt file

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
            if ButtonClick(MouseLocation()) == "Quit" and Legal_Toggle == False:      #the 3 main buttons on title screen
                running = False
            if ButtonClick(MouseLocation()) == "Begin" and Legal_Toggle == False:   #only allow clicking when legal screen isn't showing
                running = False
                import FileB                                    #stops this program, and starts the main code
            if ButtonClick(MouseLocation()) == "Legal":
                if Legal_Toggle == True:
                    Legal_Toggle = False
                    screen.fill((0,0,0))
                elif Legal_Toggle == False:                     #only show legal when needed, fill back with black when showing
                    Legal_Toggle = True



    PrintText((display_width/2), (8*display_height/30), funny_comment, 'Apple II Pro.otf', int(24*size_ratio), (255,0,0))           # prints all the text on page
    PrintText((display_width/2), (5*display_height/27), "TEST:#0054", 'Apple II ALT Pro.otf', int(140*size_ratio), (255,255,255))   #the display_width and display_height are removed functionality
    PrintText((display_width/2), (15*display_height/27), "BEGIN", 'Apple II ALT Pro.otf', int(110*size_ratio), (255,255,255))       # ran out of time to integrate them into fileB
    PrintText((display_width/2), (20*display_height/27), "QUIT", 'Apple II ALT Pro.otf', int(110*size_ratio), (255,255,255))
    PrintText((5*display_width/6), (26*display_height/27), "Developed by Samuel McKid", 'Apple II Pro.otf', int(24*size_ratio), (255,0,0))
    PrintText((1*display_width/16), (26*display_height/27), "Legal", 'Apple II Pro.otf', int(24*size_ratio), (255,0,0))

    CreateButton(6*display_width/16,13*display_height/27,10*display_width/16,17*display_height/27,'Begin')
    CreateButton(3*display_width/8,2*display_height/3,5*display_width/8,22*display_height/27,'Quit')
    CreateButton(0*display_width,25*display_height/27,1*display_width/8,1*display_height,'Legal')

    if Legal_Toggle == True:        # if legal is on then show legal
        PrintLegal()


    #reset button print variable
    ButtonLocationPrintHolder = 'Nil'
    # updates the display
    pygame.display.update()
    # clock.tick(framespersecond)
    #buttonsDict.clear()
    #resets screen size if there is a change
    display_width = int(1920*size_ratio)            #removed functionality
    display_height = int(1080*size_ratio)
    screen = pygame.display.set_mode((display_width,display_height))
    clock.tick(60)


pygame.quit()
