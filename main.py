#It begins bois

#Imports
import pygame
import pygame.event as pyev

#Globals
UP = 1073741906
DOWN= 1073741905
SPACE = 32
ESC = 27
menuOptions = {0:"none",1:"start",2:"quit"}

###funtions

##main
def main():
    pygame.init()
    print(ESC)
    currentState="none"
    screen = pygame.display.set_mode((640, 240))
    clock = pygame.time.Clock()
    clock.tick(1)
    menu()
    pygame.quit()

def selectState(option):
    if option == "menu":
        menu()
    if option == "start":
        start()
    if option == "quit":
        quit()
    if option == "prepphase":
        goPrepPhase()
    if option == "advphase":
        goAdvPhase()
##menu
def menu():
    print("Menu Opening")
    currentState = "menu"
    noOfOptions = 2
    selectedEvent = 1
    loopno=0
    while currentState == 'menu':
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.KEYDOWN:

                if event.key == DOWN: 
                    selectedEvent -= 1
                    if selectedEvent == 0:
                        selectedEvent = noOfOptions
                    print("Moved down to: "+menuOptions[selectedEvent])


                if event.key == UP:
                    selectedEvent += 1
                    if selectedEvent == noOfOptions+1:
                        selectedEvent = 1
                    print("Moved up to: "+menuOptions[selectedEvent])

                if event.key == 32:
                    if selectedEvent == 1:
                        currentState = "start"
                        print("Start selected")
                    if selectedEvent == 2:
                        currentState = "quit"
                        print("Quit selected")
    print(currentState)
    selectState(currentState)

#start
def start():
    print("Game Starting")
    currentState= 'prepphase'
    goPrepPhase()

#quit
def quit():
    exit(0)

##prep phase
def goPrepPhase():
    print("Prep Phase Has Begun")
    currentState= 'prepphase'
    while currentState == 'prepphase':
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == ESC: 
                    currentState = "menu"
                    

##adventure phase
def goAdvPhase():
    pass

###Objects

#lineup
class lineup:
    pass

#characters
class character:
    pass

def generateCharacter():
    pass

#events
class events:
    pass


#main
main()