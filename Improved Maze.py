#imports
import random
from tkinter import filedialog
from tkinter import *

#functions
def getRandEdgeCell(h, w): #selects a random tile on the maze edge
    edgeCells = []
    for cell in range(w):
        if [0, cell] not in edgeCells:
            edgeCells.append([0, cell])
    for cell in range(w):
        if [h, cell] not in edgeCells:
            edgeCells.append([h, cell])
    for cell in range(h):
        if [cell, 0] not in edgeCells:
            edgeCells.append([cell, 0])
    for cell in range(h):
        if [cell, w] not in edgeCells:
            edgeCells.append([cell, w])
    return edgeCells[random.randint(0, len(edgeCells)-1)]

def checkAdj(h, w, visited, aTile): #checks all adjacent tiles
    visitedTotal = 0
    if aTile in visited:
        return False
    for y in range(-1, 2):
        if y == 0:
            for x in range(-1, 2):
                ##print([aTile[0], aTile[1]+x])
                if [aTile[0], aTile[1]+x] in visited:
                    visitedTotal += 1
        else:
            ##print([aTile[0]+y, aTile[1]])
            if [aTile[0]+y, aTile[1]] in visited:
                visitedTotal += 1
    if visitedTotal > 1:
        return False
    else:
        return True

def getValMove(h, w, visited, aTile, weighted): #finds all valid moves from the active tile
    valMoves = []
    ##print('ACTIVE: ' + str(aTile))
    for y in range(-1, 2):
        if y == 0:
            for x in range(-1, 2):
                if 0 <= aTile[1] + x <= w and checkAdj(h, w, visited, [aTile[0], aTile[1] + x]):
                    valMoves.append([aTile[0], aTile[1]+x])
                elif x != 0 and weighted:
                    valMoves.append([])
        else:
            if 0 <= aTile[0] + y <= h and checkAdj(h, w, visited, [aTile[0]+y, aTile[1]]):
                valMoves.append([aTile[0]+y, aTile[1]])
            elif weighted:
                valMoves.append([])

    return valMoves

def getMaze(h, w, weights): #generates all maze data
    weighted = False
    if weights != [0.25, 0.25, 0.25, 0.25]:
        weighted = True
    
    maze = [['█' for x in range(w+1)] for y in range(h+1)]
    start = getRandEdgeCell(h, w)

    stack = [start] #stack tracks the tiles in the current path
    visited = [start] #visited tracks all tiles that have been visited

    while stack != []:
        ##print('Stack: ' + str(stack))
        ##print('Visited: ' + str(visited))
        aTile = stack[-1]
        maze[aTile[0]][aTile[1]] = ' '
        valMoves = getValMove(h, w, visited, aTile, weighted)
        ##print(aTile)
        ##print(valMoves)
        ##printMaze(h, w, maze)
        if weighted:
            if valMoves == [[], [], [], []]:
                stack = stack[:-1]
                continue
        else:
            if valMoves == []:
                stack = stack[:-1]
                continue
        nextMove = []
        ##print(valMoves)
        if weighted:
            while len(nextMove) == 0:
                try:
                    randMove = random.choices(range(0, 4), weights = (weights[0], weights[1], weights[2], weights[3]))
                    nextMove = valMoves[randMove[0]]
                except (TypeError, IndexError) as e:
                    continue
        else:
            randMove = random.randint(0, len(valMoves)-1)
            nextMove = valMoves[randMove]
        stack.append(nextMove)
        visited.append(nextMove)
        ##print(printMaze(h, w, start, [0, 0], maze))


    while True:
        end = getRandEdgeCell(h, w)
        if end in visited and end[0] != start[0] and end[1] != start[1]: #the end should not be on the same side as the start
            break
    return start, end, maze

def printMaze(h, w, start, end, maze): #formats maze data into a printable string
    mazeStr = ''
    ##print(start)
    ##print(end)

    top = ['█'] * (w+3)
    if start[0] == 0:
        top[start[1]+1] = 'S'
    if end[0] == 0:
        top[end[1]+1] = 'E'
    bottom = ['█'] * (w+3)
    if start[0] == h:
        bottom[start[1]+1] = 'S'
    if end[0] == h:
        bottom[end[1]+1] = 'E'

    mazeStr += ''.join(top) + '\n'
    for row in range(len(maze)):
        pre = '█'
        suf = '█'
        if start[0] == row and 0 < start[0] < h:
            if start[1] == 0:
                pre = 'S'
            else:
                suf = 'S'
        if end[0] == row and 0 < end[0] < h:
            if end[1] == 0:
                suf = 'E'
            else:
                suf = 'E'
        mazeStr += pre + ''.join(maze[row]) + suf + '\n'
    mazeStr += ''.join(bottom)
    return mazeStr

#main loop
while True:
    seedNum = random.randint(1, 1000000000) #generates maze seed
    weights = [0.25, 0.25, 0.25, 0.25]
    while True: #user inputs maze height and width
        try:
            w = int(input('Enter maze width (must be greater than two): '))
            h = int(input('Enter maze height (must be greater than two): '))
        except ValueError:
            continue
        if w > 2 and h > 2:
            w -= 1
            h -= 1
            break
    if input('Do you want to use passage bias?\n').lower().startswith('y'):
        while True:
            print('All biases must be less than one and greater than zero.')
            try:
                weights[0] = float(input('Enter vertical bias: '))
                if 1 > weights[0] > 0:
                    weights[3] = weights[0]/2 #down
                    weights[2] = (1-weights[0])/2 #right
                    weights[1] = (1-weights[0])/2 #left
                    weights[0] = weights[0]/2 #up
                    break
            except ValueError:
                continue

    if input('Do you want to use a seed?\n').lower().startswith('y'): #allows seed input for maze replication
        while True:
            try:
                seedNum = int(input('Enter seed: '))
            except ValueError:
                continue
            
    random.seed(seedNum) #init seed
    mazeData = getMaze(h, w, weights) #gets a tuple of maze data
    mazeStr = printMaze(h, w, mazeData[0], mazeData[1], mazeData[2]) #gets the maze in string form
    print(mazeStr)
    if input('Do you want to use any other functions?\n').lower().startswith('y'): #allows user to open menu of other functions
        while True:
            try:
                option = int(input('''Select a function from the following options:
1. Exit this menu
2. Save maze as text file
3. Get maze seed
4. Help\n'''))
            except ValueError:
                continue
            if option == 1:
                break
            elif option == 2: #uses tkinter to open the file saving dialog, gets the location and file, and saves the maze
                root = Tk()
                root.attributes("-topmost", True)
                root.withdraw()
                root.filename = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
                f = open(root.filename + '.txt', 'w+', encoding="utf-8")
                f.write(mazeStr)
                f.close()
                root.destroy()
            elif option == 3:
                print(seedNum)
            elif option == 4:
                print('''The maze height and maze width specify the dimensions of the maze.
A seed allows you to generate a maze that is the same as a maze you have previously generated, assuming you have the seed number and entered the same dimensions.
Exiting the menu returns you to the maze generator, but does not close the program.
Saving the maze as a text file pulls up a menu that allows you to choose a location to save the maze to, and lets you select a file name.
Getting the maze seed gives you a seed that you can input into the get seed feature to regenerate the same maze.\n''')
