import random, time

def randJoke():
    jokeNum = random.randint(1,3)
    if jokeNum == 1:
        print('What do you get when you cross a snowman with a vampire?')
        time.sleep(1)
        print('Frostbite!')
    elif jokeNum == 2:
        print("What do dentists call an astronaut's cavity?")
        time.sleep(1)
        print('A black hole!')
    else:
        print('Knock knock.')
        time.sleep(1)
        print("Who's there?")
        time.sleep(1)
        print('Interrupting cow.')
        time.sleep(1)
        print('Interrupting cow wh', end='')
        time.sleep(.50)
        print('-MOO!')
randJoke()
