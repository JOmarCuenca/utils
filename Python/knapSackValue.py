import random

"""
Code to give a possible solution to the knapSack problem 0-1
Has to ways of operation, Random and static.
This code only shows how to solve the problem and give the max optimal value.
However this code unfortunetly doesn't display the combination of items.
I am still working on it.
"""

sizeOfSack = 20
objectsW = []
objectsV = []
pathMemory = []
maxWeight = 20
numberOfObjects = 10#Due to being a recursive algorithm the max Recurssion depth for the stack is 997

#Result with the static objects should be 143 
staticObjects = [#weight/value
    [5,30],#result
    [5,27],#result
    [1,4],
    [10,11],
    [6,13],
    [5,16],#result
    [10,0],
    [5,70],#result
    [8,2],
    [7,11],
]

def genStaticObjects():
    global numberOfObjects
    i = 0
    numberOfObjects = len(staticObjects)
    while(i<numberOfObjects):
        objectsW.append(staticObjects[i][0])
        objectsV.append(staticObjects[i][1])
        i+=1

def genRandomObjects():
    global objectsV,objectsW
    objectsV = [0]*numberOfObjects
    objectsW = [0]*numberOfObjects
    i = 0
    while(i<numberOfObjects):
        objectsW[i] = random.randint(1,maxWeight)
        objectsV[i] = random.randint(0,100)
        i+=1

def init(boolean):
    #Create the memory of paths so the algorithm becomes faster
    possibilites = []
    if(boolean):#Random Objects
        genRandomObjects()
    else:#Static Objects
        genStaticObjects()
    possibilities = [-1]*(numberOfObjects)

    i = 0
    while(i<sizeOfSack+1):
        pathMemory.append(possibilities.copy())
        i+=1

def getMaxValue(i,aSpace):
    global objectsW,objectsV,numberOfObjects,pathMemory
    if(i>=numberOfObjects):
        return 0
    if(pathMemory[aSpace][i]>-1):
        return pathMemory[aSpace][i]
    w = objectsW[i]
    v = objectsV[i]
    if(aSpace == 0):#no more space
        return 0
    elif(w>aSpace or v == 0):#not enough space or value is worthless
        return getMaxValue(i+1,aSpace)
    else:
        possibility1 = getMaxValue(i+1,aSpace)#we don't add the object to the sack
        possibility2 = v + getMaxValue(i+1,aSpace-w)#we add the object to the sack
        bestValue = 0
        if(possibility2>possibility1):
            bestValue = possibility2
        else:
            bestValue = possibility1
        pathMemory[aSpace][i] = bestValue
        return bestValue

def printObjects():
    global objectsW,objectsV
    i=0
    while(i<len(objectsW)):
        print(f"{i}-> w:{objectsW[i]},v:{objectsV[i]}")
        i+=1

init(True)
printObjects()
maxValuePossible = getMaxValue(0,sizeOfSack)
print(f"The max value for this set of objects is {maxValuePossible}")