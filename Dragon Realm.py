import time, random

def enterCave(caveChoice, caves):
    print('You enter the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print("A large dragon jumps in front of you, opens its jaws and...")
    time.sleep(2)
    if caves[0] == 'Hungry':
        print('Eats you!')
    else:
        print('Gives you treasure!')

while True:
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
    while True:
        caveChoice = str(input('Which cave will you go into? (1 or 2)\n'))
        if caveChoice in '12':
            break
    caves = ['Hungry', 'Friendly']
    random.shuffle(caves)
    enterCave(caveChoice, caves)
    continueProgram = input('\nDo you want to play again?\n').lower()
    if continueProgram != 'yes':
        break
