#This program is a Guess the Number game. It generates a number between 1 and 20.
#The user then has six tries to guess the number
import random

while True:
    randomNumber = random.randint(1, 20) #generate number
    userAttempts = 0 #number of times the user has guessed
    userVictory = False #whether or not the user has won
    guess = 0 #the default guess
    print('You have started Guess the Number! You have six tries to guess a number between 1 and 20.')

    #this is a loop that exits if the user has guessed six times.
    while userAttempts < 6:
        try:
            guess = int(input('Please guess a number:') or '0') #this is the input function. it defaults to 0
        except ValueError:
            while True:
                print('bruh')
        if guess == randomNumber:
            userVictory = True 
            print('You have won!')
            break #this ends the loop because the user has won
        if guess > randomNumber: 
            print('Your guess is too high.')
        if guess < randomNumber:
            print('Your guess is too low.')
        userAttempts += 1
    if userVictory == False: #when the user guesses six times, this tells the user that they lost.
        print('You have lost!')
    restart = str(input('Type R to restart:') or 'nullInput') #asks if user wants to restart
    restartKey = 'R'
    print('')
    if restart != restartKey: #breaks the loop
        break
    
