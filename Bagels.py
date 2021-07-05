import random

def getClue(secretNumber, guess):
    clue = ''
    for number in range(3):
        if guess[number] in secretNumber and secretNumber[number] != guess[number]:
            clue += 'Fermi '
        elif secretNumber[number] == guess[number]:
            clue += 'Pico '
    if clue == '':
        clue += 'Bagels '
    return clue

while True:
    secretNumber = ''
    for i in range(3):
        secretNumber += str(random.randint(0, 9))
    attempts = 1
    print('''I am thinking of a 3-digit number. Try to guess what it is.
The clues I give are...
When I say:    That means:
Bagels         None of the digits is correct.
Pico           One digit is correct but in the wrong position.
Fermi          One digit is correct and in the right position.
I have thought of a number. You have 10 guesses.''')
    while True:
        if attempts > 10:
            print('You lost!')
            print('The secret number was ' + str(secretNumber))
            break
        while True:
            print('Guess #' + str(attempts))
            guess = str(input())
            if guess[0] == 0:
                guess2 = guess[1:]
            else:
                guess2 = guess
            try:
                guess3 = int(guess2)
            except:
                continue
            if len(guess) == 3:
                break
        if guess == secretNumber:
            print('You won!')
            break
        print(getClue(secretNumber, guess))
        attempts += 1
            
