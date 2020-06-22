import numpy as np
import pygame
import heapq
import visualizeGrid

class State(object):
    def __init__(self,x,y):
        self.gVal = 10000
        self.hVal = 0
        self.fVal = 10000
        self.x = x
        self.y = y
        self.type = 0
        self.path = None
        self.neighbors = []

    def __lt__(self,other):
        if(self.fVal == other.fVal):
            return self.gVal > other.gVal #Tie breaking Test (> = Higher G Score, < = Lower G Score)
        return self.fVal < other.fVal


def repeatedForwardAStar(grid):
    startX,startY = findAgent(grid,2)
    endX,endY = findAgent(grid,3)
    openSet = [grid[startX][startY]]
    heapq.heapify(openSet)
    closedSet = []
    expandCount = 0
    finalPathLen = 0

    while(openSet):
        expandCount = expandCount + 1
        current = openSet[0]
        if (grid[current.x][current.y].type != 2 and grid[current.x][current.y].type != 3):
            grid[current.x][current.y].type = 4
        #print(current.x)
        #print(current.y)

        if(current.x == endX and current.y == endY):
            print("Success: Path Found")
            finalPath = []
            temp = current
            finalPath.append(current)
            while(temp.path != None):
                if (grid[temp.path.x][temp.path.y].type != 2 and grid[temp.path.x][temp.path.y].type != 3):
                    finalPathLen = finalPathLen + 1
                    grid[temp.path.x][temp.path.y].type = 5
                finalPath.append(temp.path)
                temp = temp.path

            visualizeGrid.displayGridWorld(grid,"Grid World")
            return expandCount, finalPathLen
        heapq.heappop(openSet)
        closedSet.append(current)

        neighbors = current.neighbors
        for i in neighbors:
            if(i in closedSet or i.type == 1):
                continue
            tempGScore = current.gVal + 1
            if(i not in openSet):
                heapq.heappush(openSet,i)
                heapq.heapify(openSet)
            elif(tempGScore >= i.gVal):
                continue
            i.gVal = tempGScore
            i.fVal = i.gVal + manhattanDistance(i,grid[endX][endY])
            i.path = current


    #print("Final Path Length: ", finalPathLen)
    print("Failure: No Solution")
    return expandCount, finalPathLen

def repeatedBackwardAStar(grid):
    startX,startY = findAgent(grid,3)
    endX,endY = findAgent(grid,2)
    openSet = [grid[startX][startY]]
    heapq.heapify(openSet)
    closedSet = []
    expandCount = 0
    finalPathLen = 0
    while(openSet):
        expandCount = expandCount + 1
        current = openSet[0]
        if (grid[current.x][current.y].type != 2 and grid[current.x][current.y].type != 3):
            grid[current.x][current.y].type = 4
        #print(current.x)
        #print(current.y)

        if(current.x == endX and current.y == endY):
            print("Success: Path Found")
            finalPath = []
            temp = current
            finalPath.append(current)
            while(temp.path != None):
                if (grid[temp.path.x][temp.path.y].type != 2 and grid[temp.path.x][temp.path.y].type != 3):
                    finalPathLen = finalPathLen + 1
                    grid[temp.path.x][temp.path.y].type = 5
                finalPath.append(temp.path)
                temp = temp.path
            visualizeGrid.displayGridWorld(grid,"Grid World")
            return expandCount, finalPathLen
        heapq.heappop(openSet)
        closedSet.append(current)

        neighbors = current.neighbors
        for i in neighbors:
            if(i in closedSet or i.type == 1):
                continue
            tempGScore = current.gVal + 1
            if(i not in openSet):
                heapq.heappush(openSet,i)
                heapq.heapify(openSet)
            elif(tempGScore >= i.gVal):
                continue
            i.gVal = tempGScore
            i.fVal = i.gVal + manhattanDistance(i,grid[endX][endY])
            i.path = current

    print("Failure: No Solution")
    return expandCount, finalPathLen

def adaptiveAStar(gridList):
    counter = -1
    boolSuccess = False
    for grid in gridList:
        expandCount = 0
        finalPathLen = 0
        counter = counter + 1
        startX,startY = findAgent(grid,2)
        endX,endY = findAgent(grid,3)
        openSet = [grid[startX][startY]]
        heapq.heapify(openSet)
        closedSet = []
        while(openSet):
            current = openSet[0]
            if (grid[current.x][current.y].type != 2 and grid[current.x][current.y].type != 3):
                grid[current.x][current.y].type = 4
            #print(current.x)
            #print(current.y)

            if(current.x == endX and current.y == endY):
                boolSuccess = True
                print("Success: Path Found")

                finalPath = []
                temp = current
                finalPath.append(current)
                while(temp.path != None):
                    if (grid[temp.path.x][temp.path.y].type != 2 and grid[temp.path.x][temp.path.y].type != 3):
                        grid[temp.path.x][temp.path.y].type = 5
                    finalPath.append(temp.path)
                    temp = temp.path

                if(counter == 49):
                    visualizeGrid.displayGridWorld(grid,"Grid World")
                break
            heapq.heappop(openSet)
            closedSet.append(current)

            neighbors = current.neighbors
            for i in neighbors:
                if(i in closedSet or i.type == 1):
                    continue
                tempGScore = current.gVal + 1
                if(i not in openSet):
                    heapq.heappush(openSet,i)
                    heapq.heapify(openSet)
                elif(tempGScore >= i.gVal):
                    continue
                i.gVal = tempGScore
                i.fVal = i.gVal + manhattanDistance(i,grid[endX][endY])
                i.path = current
        if(boolSuccess == False):
            print("Failure: No Solution")
        if(counter != 49):
            for a in range(0,101):
                for b in range(0,101):
                    gridList[counter+1][a][b].hVal = gridList[counter][a][b].hVal
            for c in closedSet:
                gridList[counter+1][c.x][c.y].hVal = grid[endX][endY].gVal - grid[c.x][c.y].gVal


def manhattanDistance(i,end):
    return abs(i.x - end.x) + abs(i.y - end.y)


def findAgent(grid, item):
    for i in range(0,101):
        for j in range(0,101):
            if(grid[i][j].type == item):
                return i,j

def printNeighbors(neighbors):
    for i in neighbors:
        print(i.x)
        print(i.y)

def printOpenSet(openSet):
    for i in openSet:
        print(i.fVal)

def randomPosition(x,y):
    return np.random.randint(x,y)

def initGrid():
    grid = []
    for h in range(101):
        grid.append([0]*101)

    for i in range(0,101):
        for j in range(0,101):
            grid[i][j] = State(i,j)

    grid[randomPosition(0,101)][randomPosition(0,101)].type = 2
    grid[randomPosition(0,101)][randomPosition(0,101)].type = 3

    for x in range(0,101):
        for y in range(0,101):
            if grid[x][y].type != 2 and grid[x][y].type != 3 and np.random.randint(0,100) > 70:
                grid[x][y].type = 1

    for r in range(0,101):
        for t in range(0,101):
            if(r < 100):
                grid[r][t].neighbors.append(grid[r + 1][t])
            if(r > 0):
                grid[r][t].neighbors.append(grid[r - 1][t])
            if(t < 100):
                grid[r][t].neighbors.append(grid[r][t + 1])
            if(t > 0):
                grid[r][t].neighbors.append(grid[r][t - 1])


    startX,startY = findAgent(grid,2)
    endX,endY = findAgent(grid,3)
    grid[startX][startY].gVal = 0
    grid[startX][startY].fVal = manhattanDistance(grid[startX][startY],grid[endX][endY])
    return grid

def initAdaptiveGrid(constX,constY):
    grid = []
    for h in range(101):
        grid.append([0]*101)

    for i in range(0,101):
        for j in range(0,101):
            grid[i][j] = State(i,j)

    grid[randomPosition(0,101)][randomPosition(0,101)].type = 2
    grid[constX][constY].type = 3

    for x in range(0,101):
        for y in range(0,101):
            if grid[x][y].type != 2 and grid[x][y].type != 3 and np.random.randint(0,100) > 70:
                grid[x][y].type = 1

    for r in range(0,101):
        for t in range(0,101):
            if(r < 100):
                grid[r][t].neighbors.append(grid[r + 1][t])
            if(r > 0):
                grid[r][t].neighbors.append(grid[r - 1][t])
            if(t < 100):
                grid[r][t].neighbors.append(grid[r][t + 1])
            if(t > 0):
                grid[r][t].neighbors.append(grid[r][t - 1])


    startX,startY = findAgent(grid,2)
    endX,endY = findAgent(grid,3)
    grid[startX][startY].gVal = 0
    grid[startX][startY].fVal = manhattanDistance(grid[startX][startY],grid[endX][endY])
    return grid

"""
#gridWorldList to keep track of Grid Worlds
gridWorldList = []
#build 50 Grid Worlds and add them to the list and Grid World folder
for i in range(50):
    gridWorldList.append(initGrid())
#ask user which Grid World they wich to select
specifiedGridWorld = input("Please specify a Grid World (0-49) and press 'enter' on your keyboard: ")
specifiedGridWorld = int(specifiedGridWorld)
#load specified Grid World and begin
repeatedForwardAStar(gridWorldList[specifiedGridWorld])
"""
"""
gridList = []
for i in range(50):
    gridList.append(initGrid())
repeatedForwardAStar(gridList[5])

gridListAdaptive = []
for i in range(50):
    gridListAdaptive.append(initAdaptiveGrid(10,10))
adaptiveAStar(gridListAdaptive)
"""
