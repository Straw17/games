import os, time, keyboard, random
#ALL COORDS SHOULD BE IN (Y, X) FORMAT

def clear():
    os.system('cls')

def expandArray(array, scale):
    newArray = []
    for row in range(len(array)*scale):
        newArray.append([' ']*(len(array[0])*scale))
    for row in range(len(newArray)):
        for cell in range(len(newArray[row])):
            newArray[row][cell] = array[row//scale][cell//scale]
    return newArray

def display(snekStack, food):
    board = []
    for row in range(13):
        board.append([' ']*21)
    boardString = '\n' * 50
    board[food[0]][food[1]] = 'X'
    for coord in snekStack:
        board[coord[0]][coord[1]] = '█'
    board = expandArray(board, 2)
    boardString += '+' + ('-' * 42) + '+\n'
    for row in board:
        boardString += '|' + ''.join(row) + '|\n'
    boardString += '+' + ('-' * 42) + '+\n'
    print(boardString, end = '')
    time.sleep(0.1)
    print('\r' * (len(board) + 3))

def getNewStack(snekStack, snekLast, new, ate):
    snekStack.insert(0, new)
    if not ate:
        snekLast = snekStack[-1]
        snekStack = snekStack[:-1]
    return snekStack, snekLast

def getNewFood(snekStack, snekLast):
    snekStack
    snekStack.append(snekLast)
    possList = []
    for y in range(13):
        for x in range(21):
            newCoord = [y, x]
            if newCoord not in snekStack:
                possList.append(newCoord)
    return random.choice(possList)

while True:
    snekStack = [[6, 4], [6, 3], [6, 2]]
    snekLast = [6, 1]
    move = [0, 1]
    food = [6, 10]
    clear()
    while True:
        ate = False;
        if move not in [[-1, 0], [1, 0]]:
            if keyboard.is_pressed('up'):
                move = [-1, 0]
            if keyboard.is_pressed('down'):
                move = [1, 0]
        elif move not in [[0, -1], [0, 1]]:
            if keyboard.is_pressed('right'):
                move = [0, 1]
            if keyboard.is_pressed('left'):
                move = [0, -1]
        new = [snekStack[0][0]+move[0], snekStack[0][1]+move[1]]
        if new[0] < 0 or new[1] < 0 or new[0] > 12 or new[1] > 20:
            break
        if new in snekStack:
            break
        if new == food:
            ate = True
            food = getNewFood(snekStack.copy(), snekLast)
        snekStack, snekLast = getNewStack(snekStack, snekLast, new, ate)
        display(snekStack, food)
    #clear()
    print('You reached a total length of ' + str(len(snekStack)))
    print('You lost! Press the space bar to continue.')
    keyboard.wait('space')
    time.sleep(0.2)
