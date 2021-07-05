import random, math

def printBoard(board):
    boardString = ''
    for row in range(15):
        space = ''
        if row < 10:
            space = ' '
        boardString += (space + str(row) + ' ' + ''.join(board[row]) + '\n')
    print('   000000000011111111112222222222333333333344444444445555555555')
    print('   012345678901234567890123456789012345678901234567890123456789')
    print(boardString)

def generateBoard():
    board = []
    for x in range(15):
        row = []
        for x in range(60):
            row.append('~')
        board.append(row)
    return board

def placeTreasures():
    treasureCoords = []
    for treasure in range(3):
        treasureCoords.append([random.randint(0, 59), random.randint(0, 14)])
    return treasureCoords

def getInput(pastMoves):
    while True:
        print('Where do you want to move on the X axis (0-59)?')
        moveX = input()
        try:
            if -1 > int(moveX) or int(moveX) > 59:
                continue
        except ValueError:
            continue
        print('Where do you want to move on the Y axis (0-14)?')
        moveY = input()
        try:
            if -1 > int(moveY) or int(moveY) > 14:
                continue
        except ValueError:
            continue
        if [int(moveX), int(moveY)] in pastMoves:
            print('You moved there in the past.')
            continue
        return [int(moveX), int(moveY)]

def makeMove(board, treasureCoords, moveX, moveY):
    smallestDistance = 100
    for tX, tY in treasureCoords:
        distance = math.sqrt((tX - moveX) * (tX - moveX) + (tY - moveY) * (tY - moveY))
        if distance < smallestDistance:
            smallestDistance = distance
    smallestDistance = int(round(smallestDistance))
    if smallestDistance == 0:
        treasureCoords.remove([moveX, moveY])
        return '\nYou have found a treasure!\n'
    else:
        if smallestDistance < 10:
            board[moveY][moveX] = str(smallestDistance)
            return '\nTreasure detected at a distance of ' + str(smallestDistance) + ' from the sonar device.\n'
        else:
            board[moveY][moveX] = 'X'
            return '\nNo treasure detected.\n'

while True:
    board = generateBoard()
    treasureCoords = placeTreasures()
    sonarCount = 20
    pastMoves = []

    while sonarCount > 0:
        printBoard(board)
        print('You have ' + str(sonarCount) + ' sonar devices. You have found ' + str(3 - len(treasureCoords)) + ' treasure chests.')
        move = getInput(pastMoves)
        pastMoves.append(move)
        moveResult = makeMove(board, treasureCoords, move[0], move[1])
        if moveResult == '\nYou have found a treasure!\n':
            for x, y in pastMoves:
                makeMove(board, treasureCoords, x, y)
        print(moveResult)
        if len(treasureCoords) == 0:
            print('You have won!')
            break
        sonarCount -= 1
    if sonarCount == 0:
        print('You have lost!')
        print(treasureCoords + '\n')
