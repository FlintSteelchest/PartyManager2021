#It begins bois

#Imports
import pygame
import pygame.event as pyev

#Globals
UP = 1073741906
DOWN= 1073741905
SPACE = 32
ESC = 27
Party = []
###funtions

##main
def main():
    pygame.init()
    currentState="none"
    screen = pygame.display.set_mode((640, 240))
    clock = pygame.time.Clock()
    clock.tick(1)
    startMenu()
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

def startMenu():

    print("Welcome to the game!")
    print("The menu options are:")
    startMenuOptions = {1:"start",2:"quit"}
    for option in startMenuOptions.values():
        print(option)
    currentState = "menu"
    noOfOptions = 2
    selectedEvent = 1
    print("You have \""+ startMenuOptions[selectedEvent]+"\" selected")
    loopno=0
    while currentState == 'menu':
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.KEYDOWN:

                if event.key == DOWN: 
                    selectedEvent -= 1
                    if selectedEvent == 0:
                        selectedEvent = noOfOptions
                    print("Moved down to: "+startMenuOptions[selectedEvent])


                if event.key == UP:
                    selectedEvent += 1
                    if selectedEvent == noOfOptions+1:
                        selectedEvent = 1
                    print("Moved up to: "+startMenuOptions[selectedEvent])

                if event.key == 32:
                    if selectedEvent == 1:
                        currentState = "start"
                        print("Start selected")
                    if selectedEvent == 2:
                        currentState = "quit"
                        print("Quit selected")
    selectState(currentState)

def gameMenu():
    print("Welcome to the game!")
    print("The menu options are:")
    gameMenuOptions = {1:"return to game",2:"quit"}
    for option in gameMenuOptions.values():
        print(option)
    currentState = "menu"
    selectedEvent = 1
    print("You have \""+ gameMenuOptions[selectedEvent]+"\" selected")
    while currentState == 'menu':
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.KEYDOWN:

                if event.key == DOWN: 
                    selectedEvent -= 1
                    if selectedEvent == 0:
                        selectedEvent = len(gameMenuOptions)
                    print("Moved down to: "+gameMenuOptions[selectedEvent])


                if event.key == UP:
                    selectedEvent += 1
                    if selectedEvent == len(gameMenuOptions)+1:
                        selectedEvent = 1
                    print("Moved up to: "+gameMenuOptions[selectedEvent])

                if event.key == SPACE:
                    if selectedEvent == 1:
                        currentState = "start"
                        print("Start selected")
                    if selectedEvent == 2:
                        currentState = "quit"
                        print("Quit selected")
    if currentState != "return to game":
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
    global Party
    print("Prep Phase Has Begun")
    prepMenuOptions = {1:"Create random character",2:"Go on adventure"}
    currentState= 'prepphase'
    selectedEvent = 1
    
    print("You have \""+ prepMenuOptions[selectedEvent]+"\" selected")

    for option in prepMenuOptions.values():
        print(option)
    while currentState == 'prepphase':
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == DOWN: 
                    selectedEvent -= 1
                    if selectedEvent == 0:
                        selectedEvent = len(prepMenuOptions)
                    print("Moved down to: "+prepMenuOptions[selectedEvent])


                if event.key == UP:
                    selectedEvent += 1
                    if selectedEvent == len(prepMenuOptions)+1:
                        selectedEvent = 1
                    print("Moved up to: "+prepMenuOptions[selectedEvent])
                if event.key == ESC: 
                    gameMenu()
                
                if event.key == SPACE:
                    if prepMenuOptions[selectedEvent] == "Create random character":
                        character = generate_character("Bob",1,2)
                        printCharacter(character)
                        if(acceptCharacter(character)):
                            Party=[character]
                    if prepMenuOptions[selectedEvent] == "Go on adventure":
                        currentState = "advphase"
    selectState(currentState)

def acceptCharacter(char):
    print("The options are:")
    gameMenuOptions = {1:"Keep these stats",2:"I don't want them in my party"}
    for option in gameMenuOptions.values():
        print(option)
    currentState = "menu"
    noOfOptions = 2
    selectedEvent = 1
    print("You have \""+ gameMenuOptions[selectedEvent]+"\" selected")
    while currentState == 'menu':
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.KEYDOWN:

                if event.key == DOWN: 
                    selectedEvent -= 1
                    if selectedEvent == 0:
                        selectedEvent = noOfOptions
                    print("Moved down to: "+gameMenuOptions[selectedEvent])


                if event.key == UP:
                    selectedEvent += 1
                    if selectedEvent == noOfOptions+1:
                        selectedEvent = 1
                    print("Moved up to: "+gameMenuOptions[selectedEvent])

                if event.key == SPACE:
                    if selectedEvent == 1:
                        currentState = "Keep these stats"
                        print("They join your party")
                        return True
                    if selectedEvent == 2:
                        currentState = "I don't want him in my party"
                        print("They leave, sadly")
                        return False

##adventure phase
def goAdvPhase():
    print("Adv Phase Has Begun")
    currentState= 'advphase'
    skillcheck(Party[0])
    while currentState == 'advphase':
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == ESC: 
                    gameMenu()
                if event.key == SPACE:
                    currentState = "prepphase"
    selectState(currentState)

###Objects

#lineup
class lineup:
    pass

#characters
class character:
    pass

def generateCharacter():
    pass

'''character
    LVL    
    HP
    Strength
        Athletics
    Dexterity
        Acrobatics
    Constiution
    Inteligence
        Arcana
        History
        Investigation
        Nature
        Relgion
    Wisdom
        Animal Handling
        Insight
        Medicine
        Perception
        Survial  
    Charisma
        Deception
        Intimidation
        Performance
        Pesuasion'''

import random

#roll stats 4d6-1
def fourdsix ():
    roll1 = random.randint (1,6)
    roll2 = random.randint (1,6)
    roll3 = random.randint (1,6)
    roll4 = random.randint (1,6)
    total_rolls = [roll1,roll2,roll3,roll4]
    total_rolls.sort() 
    total_rolls.pop(0)
    stat = total_rolls[0] + total_rolls[1] + total_rolls[2]
    return stat

def printCharacter(char):
    for ch in char:
        for c in ch:
            print(c+":"+str(ch[c]))

def printCharacterShort(char):
    for ch in char[0:1]:
        for c in ch:
            print(c+":"+str(ch[c]))
#generate the character block
def generate_character (n,l,hd):

    #dictionaries to search for appropiate proficany and stat modifiers
    modifier = {1:-5,2:-4,3:-4,4:-3,5:-3,6:-2,7:-2,8:-1,9:-1,10:0,11:0,12:1,13:1,14:2,15:2,16:3,17:3,18:4,19:4,20:5}
    proficancy = {1:2,2:2,3:2,4:2,5:3,6:3,7:3,8:3,9:4,10:4,11:4,12:4,13:5,14:5,15:5,16:5,17:6,18:6,19:6,20:6}

    #generate core stat block
    name = {'Name':n}
    level = {'lvl' : l}
    strength = fourdsix()
    dexterity = fourdsix()
    constiution = fourdsix()
    intelegence = fourdsix()
    wisdom = fourdsix()
    charisma = fourdsix()
    hp = {'HP':6 + (sum([random.randint(1,hd) for i in range(level['lvl'])])) + modifier[constiution]*level['lvl']}

 
    listofskills =[['athletics','str'],['acrobatics','dex'],['animal handling','wis'],['arcana','int'],['deception','cha'],['history','int'],['insight','wis'],['intimidation','cha'],['investigation','int'],['medicine','wis'],['nature','int'],['perception','wis'],['persuasion','wis'],['religion','int'],['slight of hand','dex'],['stealth','dex'],['survivial','wis']]
    skilldictionary = {'str':strength,'dex':dexterity,'con':constiution,'int':intelegence,'wis':wisdom,'cha':charisma}
    
    character_stats = {'str':strength,'dex':dexterity,'con':constiution,'int':intelegence,'wis':wisdom,'cha':charisma}  
    
    #generate skill blocks
    skills = {}

    for x in listofskills :
        skills.update({x[0]:modifier[skilldictionary[x[1]]]})
        

    #generate character block
    character = [name,level,hp,character_stats,skills]
    return character



#events
class events:
    pass

#skill check
def skillcheck(character) :
    print(character)
    listofskills =[['athletics','str'],['acrobatics','dex'],['animal handling','wis'],['arcana','int'],['deception','cha'],['history','int'],['insight','wis'],['intimidation','cha'],['investigation','int'],['medicine','wis'],['nature','int'],['perception','wis'],['persuasion','wis'],['religion','int'],['slight of hand','dex'],['stealth','dex'],['survivial','wis']]
    skilltest = random.choice(list(listofskills))
    skillthreshold = random.randint(8,22)
   
    print ('Oh no!, a problem that can only be solved by '+str(skilltest[0])+' and it requires that are crew rolls a '+str(skillthreshold)+' to pass!')
    input ()
    print (character[0]['Name']+ ' steps up... ')
    #
    charroll = character [4][skilltest[0]] + random.randint(1,20)
    print (charroll) 
    if charroll >= skillthreshold :
        print ("Sucess")
    else :
        print ("Failure")


#main
main()