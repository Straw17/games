import random
#TODO: add something to show possible moves

def generateBoard():
    board = []
    for i in range(10):
        if i == 0:
            board.append(['NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL'])
        board.append(['NULL', '-', '-', '-', '-', '-', '-', '-', '-'])
    board[4][4] = 'B'
    board[5][5] = 'B'
    board[4][5] = 'W'
    board[5][4] = 'W'
    return board
    
def printBoard(board):
    print('    1 2 3 4 5 6 7 8\n')
    print('1   '+' '.join(board[1][1:]))
    print('2   '+' '.join(board[2][1:]))
    print('3   '+' '.join(board[3][1:]))
    print('4   '+' '.join(board[4][1:]))
    print('5   '+' '.join(board[5][1:]))
    print('6   '+' '.join(board[6][1:]))
    print('7   '+' '.join(board[7][1:]))
    print('8   '+' '.join(board[8][1:]))

def checkGameEnd(board):
    for turn in ['W', 'B']:
        for x in range(1, 9):
            for y in range(1, 9):
                if isValidMove(turn, x, y, board):
                    return False
    return True

def winningSide(humanColor, aiColor, board):
    humanScore = 0
    aiScore = 0
    for x in range(1, 9):
        for y in range(1, 9):
            if board[y][x] == humanColor:
                humanScore += 1
    for x in range(1, 9):
        for y in range(1, 9):
            if board[y][x] == aiColor:
                aiScore += 1
    if humanScore > aiScore:
        return 'You have won!'
    elif aiScore > humanScore:
        return 'The AI has won!'
    else:
        return 'The game is a tie!'

def playerColor():
    while True:
        print('What color do you want to play as? The choices are black or white.')
        color = str(input().lower() or 'NULL')
        if color in ['black', 'white']:
            if color == 'black':
                color = 'B'
            else:
                color = 'W'
            return color

def firstPlayer(humanColor):
    players = ['B', 'W']
    if players[1] == humanColor:
        print('You will go first.')
        return 'human'
    else:
        print('The AI will go first')
        return 'ai'

def isValidMove(color, xCor, yCor, board):
    xCor = int(xCor)
    yCor = int(yCor)
    if board[yCor][xCor] != '-':
        return False
    if color == 'W':
        otherColor = 'B'
    else:
        otherColor = 'W'
    flippableTiles = []
    for xDir, yDir in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x = xCor
        y = yCor
        x += xDir
        y += yDir
        while 0 < x < 9 and 0 < y < 9 and board[y][x] == otherColor:
            x += xDir
            y += yDir
            if 0 < x < 9 and 0 < y < 9 and board[y][x] == color:
                while True:
                    x -= xDir
                    y -= yDir
                    if x == xCor and y == yCor:
                        break
                    flippableTiles.append([x, y])
    if len(flippableTiles) == 0:
        return False
    return flippableTiles

def finalizeMove(color, move, board):
    xCor = int(move[0])
    yCor = int(move[2])
    tilesToFlip = isValidMove(color, xCor, yCor, board)
    if tilesToFlip == False:
        return False
    board[yCor][xCor] = color
    for x, y in tilesToFlip:
        board[y][x] = color
    return True

def getHumanMove(board, humanColor):
    while True:
        print('Where do you want to move? Please format all moves as column-row. Ex: 5-4.')
        move = str(input())
        try:
            move.split('-')
            xCor = int(move[0])
            yCor = int(move[2])
        except (ValueError, IndexError) as e:
            continue
        if 0 < xCor < 9 and 0 < yCor < 9 and isValidMove(humanColor, xCor, yCor, board):
            return move

def getAIMove(board, aiColor):
    bestMoveX = 0
    bestMoveY = 0
    biggestMove = 0
    
    for y in range(1, 9):
        for x in range(1, 9):
            if isValidMove(aiColor, x, y, board):
                if len(isValidMove(aiColor, x, y, board)) > biggestMove:
                    biggestMove = len(isValidMove(aiColor, x, y, board))
                    bestMoveX = x
                    bestMoveY = y
    return str(bestMoveX) + '-' + str(bestMoveY)
while True:
    board = generateBoard()
    humanColor = playerColor()
    if humanColor == 'B':
        aiColor = 'W'
    else:
        aiColor = 'B'
    turn = firstPlayer(humanColor)
    while True:
        printBoard(board)
        if turn == 'human':
            finalizeMove(humanColor, getHumanMove(board, humanColor), board)
            turn = 'AI'
        else:
            print('\nThe AI is moving...\n')
            finalizeMove(aiColor, getAIMove(board, aiColor), board)
            turn = 'human'
        if checkGameEnd(board):
            print('The game is over!')
            print(winningSide(humanColor, aiColor, board))
