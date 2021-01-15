#It begins bois

#Imports
import pygame
import pygame.event as pyev

##global variables
currentState="none"

###funtions

##main
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 240))
    clock = pygame.time.Clock()
    clock.tick(1)
    menu()
    pygame.quit()

##menu
def menu():
    currentState = "menu"
    noOfOptions = 2
    selectedEvent = 1
    loopno=0
    while currentState == 'menu':
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                print(event.key)
                if event == pygame.K_DOWN: 
                    selectedEvent -= 1
                    if selectedEvent == 0:
                        selectedEvent = noOfOptions
                        print("down")
                if event == pygame.K_UP:
                    selectedEvent += 1
                    if selectedEvent == noOfOptions+1:
                        selectedEvent = 1
                        print("up")
                if event.key == 32:
                    if selectedEvent == 1:
                        currentState = "start"
                        print("Start selected")
                    if selectedEvent == 2:
                        currentState = "quit"
                        print("Quit selected")

    if currentState=="start":
        start()
    if currentState=="quit":
        quit()

#start
def start():
    pass

#quit
def quit():
    exit(0)

##prep phase
def goPrepPhase():
    pass

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