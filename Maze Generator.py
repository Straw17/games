import random

def randOnMazeEdge(w, h):
    rand = random.randint(0, 3)
    if rand == 0:
        randCoord = [random.randint(0, w), 0]
    elif rand == 1:
        randCoord = [w, random.randint(0, h)]
    elif rand == 2:
        randCoord = [random.randint(0, w), h]
    else:
        randCoord = [0, random.randint(0, h)]
    return randCoord

def checkAdj(x, y, maze):
    try:
        if maze[y+1][x] == ' ':
            return False
    except IndexError:
        pass

    try:
        if maze[y-1][x] == ' ':
            return False
    except IndexError:
        pass

    try:
        if maze[y][x+1] == ' ':
            return False
    except IndexError:
        pass

    try:
        if maze[y][x-1] == ' ':
            return False
    except IndexError:
        pass
    
    return True

def getExpOptions(x, y, maze):
    validTiles = []

    try:
        if maze[y+1][x] != ' ':
            if checkAdj(x, y+1, maze):
                validTiles.append([y+1, x])
    except IndexError:
        pass

    try:
        if maze[y-1][x] != ' ':
            if checkAdj(x, y-1, maze):
                validTiles.append([y-1, x])
    except IndexError:
        pass

    try:
        if maze[y][x+1] != ' ':
            if checkAdj(x+1, y, maze):
                validTiles.append([y, x+1])
    except IndexError:
        pass

    try:
        if maze[y][x-1] != ' ':
            if checkAdj(x-1, y, maze):
                validTiles.append([y, x-1])
    except IndexError:
        pass

    return validTiles

def makeMaze(w, h):
    maze = [['+' for x in range(w)] for y in range(h)]
    w -= 1
    h -= 1

    start = randOnMazeEdge(w, h)
    stack = [start]

    while stack != []:
        aTile = stack[len(stack)-1]
        maze[aTile[1]][aTile[0]] = 'X'
        validTiles = getExpOptions(aTile[1], aTile[0], maze)
        print(validTiles)
        for tile in validTiles:
            maze[tile[1]][tile[0]] = 'X'
        break

    return maze

def printMaze(maze):
    for row in maze:
        print(''.join(row))
    print()

maze = makeMaze(20, 20)
printMaze(maze)
