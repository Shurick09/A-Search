import computePath
import time


def comparingAlgosTime():
    gridListForward = []
    start = time.time()
    for i in range(50):
        gridListForward.append(computePath.initGrid())
        computePath.repeatedForwardAStar(gridListForward[i])
    end = time.time()
    repeatedForwardTime = (end - start) / 50

    print("Forward",repeatedForwardTime)

    gridListBackward = []
    start2 = time.time()
    for j in range(50):
        gridListBackward.append(computePath.initGrid())
        computePath.repeatedBackwardAStar(gridListBackward[j])
    end2 = time.time()
    repeatedBackwardTime = (end2 - start2) / 50

    print("Backward", repeatedBackwardTime)


    gridListAdaptive = []
    start3 = time.time()
    for k in range(50):
        gridListAdaptive.append(computePath.initAdaptiveGrid(10,10))
    computePath.adaptiveAStar(gridListAdaptive)
    end3 = time.time()
    adaptiveTime = (end3 - start3) / 50

    print("Forward Repeated A*", repeatedForwardTime)
    print("Backward Repeated A*", repeatedBackwardTime)
    print("Adaptive", adaptiveTime)

def comparingAlgosExpansions():
    gridListForward = []
    totExpansions = 0
    totFinalPathLen = 0
    """
    for i in range(50):
        gridListForward.append(computePath.initGrid())
        expansions, finalPathLen = computePath.repeatedForwardAStar(gridListForward[i])
        totExpansions = totExpansions + expansions
        totFinalPathLen = totFinalPathLen + finalPathLen

    repeatedForwardExpansions = float(totExpansions) / 50
    repeatedForwardFinalPathLen = float(totFinalPathLen) / 50

    print("Forward Expansions ",repeatedForwardExpansions)
    print("Forward Final Path Length ", repeatedForwardFinalPathLen)

    """
    totExpansions1 = 0
    totFinalPathLen1 = 0
    gridListBackward = []

    for j in range(50):
        gridListBackward.append(computePath.initGrid())
        expansions1, finalPathLen1 = computePath.repeatedBackwardAStar(gridListBackward[j])
        totExpansions1 = totExpansions1 + expansions1
        totFinalPathLen1 = totFinalPathLen1 + finalPathLen1

    repeatedBackwardExpansions = float(totExpansions1) / 50
    repeatedBackwardFinalPathLen = float(totFinalPathLen1) / 50

    print("Backward Expansions ",repeatedBackwardExpansions)
    print("Backward Final Path Length ", repeatedBackwardFinalPathLen)


    """
    gridListAdaptive = []
    start3 = time.time()
    for k in range(50):
        gridListAdaptive.append(computePath.initAdaptiveGrid(10,10))
    computePath.adaptiveAStar(gridListAdaptive)
    end3 = time.time()
    adaptiveTime = (end3 - start3) / 50

    print("Forward Repeated A*", repeatedForwardTime)
    #print("Backward Repeated A*", repeatedBackwardTime)
    print("Adaptive", adaptiveTime)
    """

def comparingTieBreaking():
    gridListForward = []
    start = time.time()
    for i in range(50):
        gridListForward.append(computePath.initGrid())
        computePath.repeatedForwardAStar(gridListForward[i])
    end = time.time()
    repeatedForwardTime = (end - start) / 50

    print("Repeated Forward A* (Lower G Score)",repeatedForwardTime)

def demoTest():
    whichSearch = input("Which search do you want to test? (0 = Forward, 1 = Backward, 2 = Adaptive)? ")
    whichSearch = int(whichSearch)
    if(whichSearch == 0):
        #gridWorldList to keep track of Grid Worlds
        gridWorldList = []
        #build 50 Grid Worlds and add them to the list and Grid World folder
        for i in range(50):
            gridWorldList.append(computePath.initGrid())
        #ask user which Grid World they wich to select
        specifiedGridWorld = input("Please specify a Grid World (0-49) and press 'enter' on your keyboard: ")
        specifiedGridWorld = int(specifiedGridWorld)
        #load specified Grid World and begin
        computePath.repeatedForwardAStar(gridWorldList[specifiedGridWorld])

    elif(whichSearch == 1):
        gridWorldBackward = []
        for j in range(50):
            gridWorldBackward.append(computePath.initGrid())
        #ask user which Grid World they wich to select
        specifiedGridWorldBackward = input("Please specify a Grid World (0-49) and press 'enter' on your keyboard: ")
        specifiedGridWorldBackward = int(specifiedGridWorldBackward)
        #load specified Grid World and begin
        computePath.repeatedForwardAStar(gridWorldBackward[specifiedGridWorldBackward])

    elif(whichSearch == 2):
        gridListAdaptive = []
        for i in range(50):
            gridListAdaptive.append(computePath.initAdaptiveGrid(10,10))
        computePath.adaptiveAStar(gridListAdaptive)

#comparingAlgosTime()
demoTest()
#comparingTieBreaking()
#comparingAlgosExpansions()
