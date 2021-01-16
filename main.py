#It begins bois

#Imports
import pygame
import pygame.event as pyev
import random
import csv
#Globals
STATS = ["STR","DEX","CON","WIS","INT","CHA"]
UP = 1073741906
DOWN= 1073741905
SPACE = 32
ESC = 27
Party = []
HISTORY = ["","","","","","","","","",""]
###funtions

##main
pygame.init()
pygame.font.init()
currentState="none"
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Party Manager Sim 2021')

clock = pygame.time.Clock()
clock.tick(10)

def main():
    startMenu()
    pygame.quit()

def printToScreen(text):
    print(text)
    temp = HISTORY.copy()
    temp.insert(0,text)
    print(temp)
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)    
    font = pygame.font.SysFont('Comic Sans MS', 30)
    display_surface = pygame.display.set_mode((640, 480))
    for message in range(1,9):
        text = font.render(temp[message], True, green, blue)
        textRect = text.get_rect()
        textRect.center = (320,412-48*message)
        display_surface.blit(text, textRect)
    text = font.render(temp[0], True, blue, green)
    textRect = text.get_rect()
    textRect.center = (320,460)
    display_surface.blit(text, textRect)

    pygame.display.update()

def printToScreenHistory(text):
    print(text)
    HISTORY.insert(0,text)
    print(HISTORY)
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)    
    font = pygame.font.SysFont('Comic Sans MS', 30)
    display_surface = pygame.display.set_mode((640, 480))
    for message in range(1,9):
        text = font.render(HISTORY[message], True, green, blue)
        textRect = text.get_rect()
        textRect.center = (320,412-48*message)
        display_surface.blit(text, textRect)
    text = font.render(HISTORY[0], True, blue, green)
    textRect = text.get_rect()
    textRect.center = (320,460)
    display_surface.blit(text, textRect)

    pygame.display.update()


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

def genericMenu(openMessageList,menuOptions,startState,optionResultsList):
    printToScreenHistory("hello")
    for message in openMessageList:
        printToScreenHistory(message)
    printToScreenHistory("The menu options are:")
    for option in menuOptions:
        printToScreenHistory(option)
    currentState = startState
    selectedEvent = 1
    printToScreen(menuOptions[selectedEvent])

    while currentState == startState:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == DOWN: 
                    selectedEvent -= 1
                    if selectedEvent < 0:
                        selectedEvent = len(menuOptions)-1
                    printToScreen(menuOptions[selectedEvent])

                if event.key == UP:
                    selectedEvent += 1
                    if selectedEvent == len(menuOptions):
                        selectedEvent = 1
                    printToScreen(menuOptions[selectedEvent])
                
                if event.key == 32:
                    printToScreenHistory(menuOptions[selectedEvent]+" selected")
                    optionResultsList[menuOptions[selectedEvent]]()

def startMenu():
    printToScreenHistory("Welcome to the game!")
    printToScreenHistory("The menu options are:")
    startMenuOptions = {1:"start",2:"quit"}
    for option in startMenuOptions.values():
        printToScreenHistory(option)
    currentState = "menu"
    noOfOptions = 2
    selectedEvent = 1
    printToScreen(startMenuOptions[selectedEvent])
    loopno=0
    while currentState == 'menu':
        pygame.display.update()
        for event in pygame.event.get():
            #printToScreen(event)
            if event.type == pygame.KEYDOWN:

                if event.key == DOWN: 
                    selectedEvent -= 1
                    if selectedEvent == 0:
                        selectedEvent = noOfOptions
                    printToScreen(startMenuOptions[selectedEvent])


                if event.key == UP:
                    selectedEvent += 1
                    if selectedEvent == noOfOptions+1:
                        selectedEvent = 1
                    printToScreen(startMenuOptions[selectedEvent])

                if event.key == 32:
                    if selectedEvent == 1:
                        currentState = "start"
                        printToScreenHistory("Start selected")
                    if selectedEvent == 2:
                        currentState = "quit"
                        printToScreenHistory("Quit selected")
    selectState(currentState)

def gameMenu():
    printToScreenHistory("You have paused the game")
    printToScreenHistory("The menu options are:")
    gameMenuOptions = {1:"return to game",2:"quit"}
    for option in gameMenuOptions.values():
        printToScreenHistory(option)
    currentState = "menu"
    selectedEvent = 1
    printToScreen(gameMenuOptions[selectedEvent])
    while currentState == 'menu':
        for event in pygame.event.get():
            #printToScreen(event)
            if event.type == pygame.KEYDOWN:

                if event.key == DOWN: 
                    selectedEvent -= 1
                    if selectedEvent == 0:
                        selectedEvent = len(gameMenuOptions)
                    printToScreen(gameMenuOptions[selectedEvent])


                if event.key == UP:
                    selectedEvent += 1
                    if selectedEvent == len(gameMenuOptions)+1:
                        selectedEvent = 1
                    printToScreen(gameMenuOptions[selectedEvent])

                if event.key == SPACE:
                    if selectedEvent == 1:
                        currentState = "start"
                        printToScreenHistory("Start selected")
                    if selectedEvent == 2:
                        currentState = "quit"
                        printToScreenHistory("Quit selected")
    if currentState != "return to game":
        selectState(currentState)

#start
def start():
    printToScreenHistory("Game Starting")
    currentState= 'prepphase'
    goPrepPhase()

#quit
def quit():
    exit(0)

def returntogame():
    pass

##prep phase
def goPrepPhase():
    global Party
    printToScreenHistory("Prep Phase Has Begun")
    prepMenuOptions = {1:"Create random character",2:"Go on adventure"}
    currentState= 'prepphase'
    selectedEvent = 1
    
    for option in prepMenuOptions.values():
        printToScreenHistory(option)

    while currentState == 'prepphase':
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == DOWN: 
                    selectedEvent -= 1
                    if selectedEvent == 0:
                        selectedEvent = len(prepMenuOptions)
                    printToScreen(prepMenuOptions[selectedEvent])


                if event.key == UP:
                    selectedEvent += 1
                    if selectedEvent == len(prepMenuOptions)+1:
                        selectedEvent = 1
                    printToScreen(prepMenuOptions[selectedEvent])
                if event.key == ESC: 
                    genericMenu(["You have paused the game"],["quit", "return to game"],"pause",{"quit":quit,"return to game":returntogame})
                    #gameMenu()
                
                if event.key == SPACE:
                    if prepMenuOptions[selectedEvent] == "Create random character":
                        character = generate_character("Bob",1)
                        printToScreenHistoryCharacter(character)
                        if(acceptCharacter(character)):
                            Party=[character]
                    if prepMenuOptions[selectedEvent] == "Go on adventure":
                        currentState = "advphase"
    selectState(currentState)

def acceptCharacter(char):
    printToScreenHistory("The options are:")
    gameMenuOptions = {1:"Keep these stats",2:"I don't want them in my party"}
    for option in gameMenuOptions.values():
        printToScreenHistory(option)
    currentState = "menu"
    noOfOptions = 2
    selectedEvent = 1
    printToScreen(gameMenuOptions[selectedEvent])
    while currentState == 'menu':
        for event in pygame.event.get():
            #printToScreen(event)
            if event.type == pygame.KEYDOWN:

                if event.key == DOWN: 
                    selectedEvent -= 1
                    if selectedEvent == 0:
                        selectedEvent = noOfOptions
                    printToScreen(gameMenuOptions[selectedEvent])


                if event.key == UP:
                    selectedEvent += 1
                    if selectedEvent == noOfOptions+1:
                        selectedEvent = 1
                    printToScreen(gameMenuOptions[selectedEvent])

                if event.key == SPACE:
                    if selectedEvent == 1:
                        currentState = "Keep these stats"
                        printToScreenHistory("They join your party")
                        return True
                    if selectedEvent == 2:
                        currentState = "I don't want him in my party"
                        printToScreenHistory("They leave, sadly")
                        return False

##adventure phase
def goAdvPhase():
    printToScreenHistory("Adv Phase Has Begun")
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

#roll stats 4d6-1
#number of dice, dice sides, how many to keep, how many to drop, drop high or low
def rolldice(n,s,d,hol):
    total_rolls = [random.randint(1,s) for i in range(n)]
    if d >0:
        if hol=='h':
            for x in range(d-1):
                total_rolls.remove(min(total_rolls))
        if hol=='l':
            for x in range(d-1):
                total_rolls.remove(max(total_rolls))
    stat = sum(total_rolls)
    return stat

def printCharacter(char):
    for ch in char:
        for c in ch:
            printToScreenHistory(c+":"+str(ch[c]))

def printCharacterShort(char):
    for ch in char[0:1]:
        for c in ch:
            printToScreenHistory(c+":"+str(ch[c]))
#generate the character block

#generate random class
def generate_class () :
    # hitdie + saving throws + potential proficancies + number of proficancies
    barb = [[12],['str','con'],['animal handling', 'athletics','intimidation','nature','perception','survivial'],[2]]
    bard = [[8],['dex','cha'],['athletics','acrobatics','animal handling','arcana','deception','history','insight','intimidation','investigation','medicine','nature','perception','persuasion','religion','slight of hand','stealth','survivial',],[3]]
    cler = [[8],['wis','cha'],['history', 'insight','medicine','persuasion','religion'],[2]]
    drui = [[8],['int','wis'],['arcana','animal handling', 'insight','medicine','nature','perception','religion','survivial'],[2]]
    figh = [[10],['str','con'],['acrobatics','animal handling', 'athletics','history','insight','intimidation','perception','survivial'],[2]]
    monk = [[8],['str','dex'],['acrobatics', 'athletics','history','insight','religion','stealth'],[2]]
    pala = [[10],['wis','cha'],['athletics','insight','intimidation','persuasion','religion'],[2]]
    rang = [[10],['str','cha'],['animal handling', 'athletics','insight','investigation','nature','perception','stealth','survial'],[2]]
    rogu = [[8],['dex','int'],['acrobatics', 'athletics','deception','insight','intimidation','investigation','perception','performance','persuasion','slight of hand','stealth'],[2]]
    sorc = [[6],['con','cha'],['arcana', 'deception','insight','intimidation','persuasion','religion'],[2]]
    warl = [[8],['wis','cha'],['arcana', 'deception','history','intimidation','investigation','nature','religion'],[2]]
    wiza = [[6],['int','wis'],['arcana', 'history','insight','investigation','medicine','religion'],[2]]


    classes = {'Barbarian':barb,'Bard':bard,'Cleric':cler,'Druid':drui,'Fighter':figh,'Monk':monk,'Paladin':pala,'Ranger':rang,'Rogue':rogu,'Sorcerer':sorc,'Warlock':warl,'Wizard':wiza}
    characterclass = random.choice(list(classes.items()))


    characterclass[1][2] = random.sample(characterclass[1][2],2)
    characterclass[1].pop()

    return characterclass

#generate a random race
def generate_race () :
    #racelist [Race[0],Str[1],Dex[2],Con[3],Int[4],Wis[5],Cha[6],Ran[7]]
    racelst = []
    with open ('Races - Races.csv',newline= '') as csvfile:
        sheetreader = csv.reader(csvfile, quotechar='|')
        csvfile.readline()
        for row in sheetreader :
            racelst.append(row)

    for item in racelst :
        ranstat = item[7]
        ranstat = int(ranstat)
        while not ranstat == 0 :
            x = item.index(random.choice(item[1:6]))
            #item[x] = item[x] + 1
            y = item[x]
            y = int(y) + 1
            item[x] = y

            ranstat = int(ranstat) - 1 
        item.pop()
    race = random.choice(racelst)
    #[Race,Str,Dex,Con,Int,Wis,Cha]
    return race


#roll stats 4d6-1
#number of dice, dice sides, how many to keep, how many to drop, drop high or low
def rolldice(n,s,d,hol):
    total_rolls = [random.randint(1,s) for i in range(n)]
    if d >0:
        if hol=='h':
            for x in range(d-1):
                total_rolls.remove(min(total_rolls))
        if hol=='l':
            for x in range(d-1):
                total_rolls.remove(max(total_rolls))
    stat = sum(total_rolls)
    return stat




#generate the character block
def generate_character (n,l):

    #dictionaries to search for appropiate proficany and stat modifiers
    modifier = {1:-5,2:-4,3:-4,4:-3,5:-3,6:-2,7:-2,8:-1,9:-1,10:0,11:0,12:1,13:1,14:2,15:2,16:3,17:3,18:4,19:4,20:5}
    proficancy = {1:2,2:2,3:2,4:2,5:3,6:3,7:3,8:3,9:4,10:4,11:4,12:4,13:5,14:5,15:5,16:5,17:6,18:6,19:6,20:6}
    
    #assign a race 
    race = generate_race()
    racestr = int(race[1])
    racedex = int(race[2])
    racecon = int(race[3])
    raceint = int(race[4])
    racewis = int(race[5])
    racecha = int(race[6])

    #assign class
    #outpit format Hit Die/SavingThrows/PotentialProficancies
    charclass = generate_class ()
    #hd = [charclass[0]]
    hd = charclass[1][0][0]

    #generate core stat block
    name = {'Name':n,'Race':race[0],'Class':charclass[0]}
    level = {'lvl' : l}
    strength = rolldice(4,6,3,'h') + racestr 
    dexterity = rolldice(4,6,3,'h') + racedex
    constiution = rolldice(4,6,3,'h') + racecon
    intelegence = rolldice(4,6,3,'h') + raceint
    wisdom = rolldice(4,6,3,'h') + racewis
    charisma = rolldice(4,6,3,'h') + racecha
    hp = {'HP':6 + (sum([random.randint(1,hd) for i in range(level['lvl'])])) + modifier[constiution]*level['lvl']}

 
    listofskills =[['athletics','str'],['acrobatics','dex'],['animal handling','wis'],['arcana','int'],['deception','cha'],['history','int'],['insight','wis'],['intimidation','cha'],['investigation','int'],['medicine','wis'],['nature','int'],['perception','wis'],['persuasion','wis'],['religion','int'],['slight of hand','dex'],['stealth','dex'],['survivial','wis']]
    skilldictionary = {'str':strength,'dex':dexterity,'con':constiution,'int':intelegence,'wis':wisdom,'cha':charisma}
    
    character_stats = {'str':strength,'dex':dexterity,'con':constiution,'int':intelegence,'wis':wisdom,'cha':charisma}  
    
    #generate skill blocks
    skills = {}


    for x in listofskills :
        skills.update({x[0]:modifier[skilldictionary[x[1]]]})

    for x in (charclass[1][2]) :
        y = skills[x]
        y = y + proficancy[level['lvl']]
        skills.update({x:y})
        
    #generate item block

    items = {}    

    #generate character block
    character = [name,level,hp,character_stats,skills,items]
    return character


#events
class events:
    pass

#skill check
def skillcheck(character) :
    currentState = "skillcheck"
    printToScreenHistory(character)
    listofskills =[['athletics','str'],['acrobatics','dex'],['animal handling','wis'],['arcana','int'],['deception','cha'],['history','int'],['insight','wis'],['intimidation','cha'],['investigation','int'],['medicine','wis'],['nature','int'],['perception','wis'],['persuasion','wis'],['religion','int'],['slight of hand','dex'],['stealth','dex'],['survivial','wis']]
    skilltest = random.choice(list(listofskills))
    skillthreshold = random.randint(8,22)
   
    printToScreenHistory ('Oh no!, a problem that can only be solved by '+str(skilltest[0])+' and it requires that are crew rolls a '+str(skillthreshold)+' to pass!')
    while currentState == 'skillcheck':
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == SPACE: 
                    printToScreenHistory (character[0]['Name']+ ' steps up... ')
                    #
                    if skilltest[0] in character[4]:
                        charroll = character [4][skilltest[0]] + random.randint(1,20)
                    else:
                        charroll = random.randint(1,20)
                    printToScreenHistory (charroll) 
                    if charroll >= skillthreshold :
                        printToScreenHistory ("Sucess")
                    else :
                        printToScreenHistory ("Failure")
                    currentState = 'none'


def addToChar(stats, bonus, character):
    for stat in stats:
        if stat[0] in character[stat[1]]:
            character[stat[1]][stat[0]] += bonus
        else:
            character[stat[1]][stat[0]]=bonus


class Trait:
    def __init__(self, n, c, a, r):
        self.name = n
        self.category = c
        self.add = a
        self.remove = r
    def addTrait(self,character):
        self.add[0]([[self.name,1]],1,character)
        self.add[0]([[self.add[1],self.add[2]]],self.add[3],character)

#main
main()