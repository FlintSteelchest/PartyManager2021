import random
def rolldice(n,s,d,hol):
    total_rolls = [random.randint(1,s) for i in range(n)]
    if d >0:
        if hol=='h':
            for x in range(d-1):
                print(total_rolls)
                total_rolls.remove(min(total_rolls))
        if hol=='l':
            for x in range(d-1):
                total_rolls.remove(max(total_rolls))
    stat = sum(total_rolls)
    return stat

def fourdsix ():
    roll1 = random.randint (1,6)
    roll2 = random.randint (1,6)
    roll3 = random.randint (1,6)
    roll4 = random.randint (1,6)
    total_rolls = [roll1,roll2,roll3,roll4]
    total_rolls.sort() 
    total_rolls.pop(0)
    stat = total_rolls[0:2]
    return stat

rolldice(4,6,3,'h')