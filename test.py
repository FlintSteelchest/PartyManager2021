import random
STATS = ["STR","DEX","CON","WIS","INT","CHA"]

def addToChar(stats, bonus, character):
    for stat in stats:
        if stat[0] in character[stat[1]]:
            character[stat[1]][stat[0]] += bonus
        else:
            character[stat[1]][stat[0]]=bonus
def generate_character(n,l,hd):
    
    #dictionaries to search for appropiate proficany and stat modifiers
    modifier = {1:-5,2:-4,3:-4,4:-3,5:-3,6:-2,7:-2,8:-1,9:-1,10:0,11:0,12:1,13:1,14:2,15:2,16:3,17:3,18:4,19:4,20:5}
    proficancy = {1:2,2:2,3:2,4:2,5:3,6:3,7:3,8:3,9:4,10:4,11:4,12:4,13:5,14:5,15:5,16:5,17:6,18:6,19:6,20:6}

    #generate core stat block
    name = {'Name':n}
    level = {'lvl' : l}
    strength = rolldice(4,6,3,'h')
    dexterity = rolldice(4,6,3,'h')
    constiution = rolldice(4,6,3,'h')
    intelegence = rolldice(4,6,3,'h')
    wisdom = rolldice(4,6,3,'h')
    charisma = rolldice(4,6,3,'h')
    hp = {'HP':6 + (sum([random.randint(1,hd) for i in range(level['lvl'])])) + modifier[constiution]*level['lvl']}
 
    listofskills =[['athletics','str'],['acrobatics','dex'],['animal handling','wis'],['arcana','int'],['deception','cha'],['history','int'],['insight','wis'],['intimidation','cha'],['investigation','int'],['medicine','wis'],['nature','int'],['perception','wis'],['persuasion','wis'],['religion','int'],['slight of hand','dex'],['stealth','dex'],['survivial','wis']]
    skilldictionary = {'str':strength,'dex':dexterity,'con':constiution,'int':intelegence,'wis':wisdom,'cha':charisma}
    
    character_stats = {'str':strength,'dex':dexterity,'con':constiution,'int':intelegence,'wis':wisdom,'cha':charisma}  
    
    #generate skill blocks
    skills = {}

    #generate character block
    character = [name,level,hp,character_stats,skills]
    return character

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

class Trait:
    def __init__(self, n, c, a, r):
        self.name = n
        self.category = c
        self.add = a
        self.remove = r
    def addTrait(self,character):
        for a in self.add:
            print("Here",a)
            a[0]([[self.name,1]],1,character)
            a[0]([[a[1],a[2]]],a[3],character)
    def removeTrait(self,character):
        for r in self.remove:
            r[0]([[self.name,1]],1,character)
            r[0]([[r[1],r[2]]],r[3],character)
    def __str__(self):
        return "This is the %s, it provides %s" % (self.name, self.add)
aBag = Trait(
    "A Bag",
    "item",
    [[addToChar, "Ugliness", 4, -5]],
    [[addToChar, "Ugliness", 4, 5]])

character = generate_character("Bob",1,2)
print(character)
addToChar([["Ugliness",4]],5,character)
print(character)
aBag.addTrait(character)
print(character)

import csv
items=[]
with open("Traits_and_Items2.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        items.append([row[0],row[1],row[2],row[3]])

def parseEffect(effect):
    output = []
    effect = effect.split(',')
    for e in effect:
        print(e)
        e = str(e.upper())
        if e == "No Effect":
            print("YOU GET NOTHING")
        if e.split(" ")[1] in STATS:
            output.append([addToChar,e.split(" ")[1],2,int(e.split(" ")[0])])
        else:
            print("not yet!")
    print("DONE",output)
    return output
            

for item in items:
    print(item)
    item = Trait(item[0],item[1],parseEffect(item[2]),parseEffect(item[3]))
    print(item)
    item.addTrait(character)
print(character)

printToScreen()
    pygame.font.init() # you have to call this at the start, 
                    # if you want to use this module.
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Some Text', False, (0, 0, 0))
    screen.blit(textsurface,(0,0))
