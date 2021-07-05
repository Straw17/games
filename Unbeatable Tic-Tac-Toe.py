import random

def difSelect():
    while True:
        print('What difficulty do you want? The options are: easy, medium, hard, impossible.')
        choice = str(input()).lower()
        if choice in ['easy', 'medium', 'hard', 'impossible']:
            return choice

def chooseSymbol():
    while True:
        print('What symbol do you want to use?')
        choice = str(input()).upper()
        if choice == 'X':
            return ['X', 'O']
        if choice == 'O':
            return ['O', 'X']

def firstPlayer(difficulty):
    num = random.randint(1,2)
    if difficulty == 'impossible':
        print('The AI will go first.')
        return 'AI'
    if num == 1:
        print('The AI will go first.')
        return 'AI'
    else:
        print('You will go first.')
        return 'human'

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def copyBoard(board):
    copy = []
    for space in board:
        copy.append(space)
    return copy
        
def spaceStatus(board, move):
    return str(board[int(move)]) in '123456789'

def checkWin(board, symbol):
    #printBoard(board)
    return ((board[1] == symbol and board[2] == symbol and board[3] == symbol) or # across the top
    (board[4] == symbol and board[5] == symbol and board[6] == symbol) or #across the middle
    (board[7] == symbol and board[8] == symbol and board[9] == symbol) or #across the bottom
    (board[1] == symbol and board[4] == symbol and board[7] == symbol) or #down the left side
    (board[2] == symbol and board[5] == symbol and board[8] == symbol) or #down the middle
    (board[3] == symbol and board[6] == symbol and board[9] == symbol) or #down the right side
    (board[1] == symbol and board[5] == symbol and board[9] == symbol) or #diagonal
    (board[3] == symbol and board[5] == symbol and board[7] == symbol)) #diagonal

def checkTie(board):
    tie = True
    for num in range(1, 10):
        if str(num) == board[num]:
            tie = False
            return False
    if tie == True:
        return True

def getHumanMove(board):
    move = 0
    while True:
        print('What is your next move?')
        move = input()
        if str(move) in '123456789' and spaceStatus(board, move):
            break
    return int(move)

def chooseRandom(board, moveList):
    validMoves = []
    for move in moveList:
        if spaceStatus(board, move):
            validMoves.append(move)
    if len(validMoves) == 0:
        return 'INVALID'
    else:
        randomMove = random.randint(0,len(validMoves)-1)
        return validMoves[randomMove]

def testForFork(board, move, symbol):
    copy = copyBoard(board)
    finalizeMove(copy, move, symbol)
    winningMoves = 0
    for i in range(1, 10):
        if checkWin(copy, symbol) and spaceStatus(copy, i):
            winningMoves += 1
    return winningMoves >= 2

def getAIMove(board, humanSymbol, aiSymbol, difficulty):
    if difficulty == 'easy':
        return easyDifficulty(board)
    if difficulty == 'medium':
        return mediumDifficulty(board, humanSymbol, aiSymbol)
    if difficulty == 'hard':
        return hardDifficulty(board, humanSymbol, aiSymbol)
    if difficulty == 'impossible':
        return impossibleDifficulty(board, humanSymbol, aiSymbol)

def easyDifficulty(board):
    return chooseRandom(board, [1,2,3,4,5,6,7,8,9])

def mediumDifficulty(board, humanSymbol, aiSymbol):
    for space in range(1, 10):
        copy = copyBoard(board)
        if spaceStatus(copy, space):
            copy = finalizeMove(copy, space, aiSymbol)
            if checkWin(copy, aiSymbol):
                return space
    for space in range(1, 10):
        copy = copyBoard(board)
        if spaceStatus(copy, space):
            copy = finalizeMove(copy, space, humanSymbol)
            if checkWin(copy, humanSymbol):
                return space
    move = chooseRandom(board, [1, 3, 7, 9])
    if move != 'INVALID':
        return move
    if spaceStatus(board, 5):
        return 5
    return chooseRandom(board, [2, 4, 6, 8])

def hardDifficulty(board, humanSymbol, aiSymbol):
    for space in range(1, 10):
        copy = copyBoard(board)
        if spaceStatus(copy, space):
            copy = finalizeMove(copy, space, aiSymbol)
            if checkWin(copy, aiSymbol):
                return space
    for space in range(1, 10):
        copy = copyBoard(board)
        if spaceStatus(copy, space):
            copy = finalizeMove(copy, space, humanSymbol)
            if checkWin(copy, humanSymbol):
                return space
    for space in range(1, 10):
        if spaceStatus(board, space) and testForFork(board, space, aiSymbol):
            return space
    for space in range(1, 10):
        if spaceStatus(board, space) and testForFork(board, space, humanSymbol):
            return space
    move = chooseRandom(board, [1, 3, 7, 9])
    if move != 'INVALID':
        return move
    if spaceStatus(board, 5):
        return 5
    return chooseRandom(board, [2, 4, 6, 8])

def impossibleDifficulty(board, humanSymbol, aiSymbol):
    for space in range(1, 10):
        copy = copyBoard(board)
        if spaceStatus(copy, space):
            copy = finalizeMove(copy, space, aiSymbol)
            if checkWin(copy, aiSymbol):
                return space
    for space in range(1, 10):
        copy = copyBoard(board)
        if spaceStatus(copy, space):
            copy = finalizeMove(copy, space, humanSymbol)
            if checkWin(copy, humanSymbol):
                return space
    for space in range(1, 10):
        if spaceStatus(board, space) and testForFork(board, space, aiSymbol):
            return space
    for space in range(1, 10):
        if spaceStatus(board, space) and testForFork(board, space, humanSymbol):
            return space
    if spaceStatus(board, 5):
        return 5
    move = chooseRandom(board, [1, 3, 7, 9])
    if move != 'INVALID':
        return move
    return chooseRandom(board, [2, 4, 6, 8])

def finalizeMove(board, move, symbol):
    board[move] = symbol
    return board

while True:
    print('\nStarting a new game...')
    difficulty = difSelect()
    symbols = chooseSymbol()
    humanSymbol = symbols[0]
    aiSymbol = symbols[1]
    
    turn = firstPlayer(difficulty)
    board = ['NULL', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    gameOver = False
    
    while gameOver == False:
        if turn == 'human':
            printBoard(board)
            board = finalizeMove(board, getHumanMove(board), humanSymbol)
            if checkWin(board, humanSymbol):
                print('You have won!')
                gameOver = True
        else:
            board = finalizeMove(board, getAIMove(board, humanSymbol, aiSymbol, difficulty), aiSymbol)
            if checkWin(board, aiSymbol):
                printBoard(board)
                print('The AI has won!')
                gameOver = True
        if checkTie(board) and gameOver == False:
            printBoard(board)
            print('The game is a tie!')
            gameOver = True
        if turn == 'human':
            turn = 'AI'
        else:
            turn = 'human'
