import time
import re
from AoC import inputData

start_time = time.time()

#0 Test Short
#1 Actual live data
dataSet = 1


if dataSet == 0:
    dataInput = inputData('test17.txt')
if dataSet == 1:
    dataInput = inputData('input17.txt')

def createTransform():
    outputData = []
    for x in range(-1,2):
        for y in range(-1,2):
            for z in range(-1,2):
                if not (x == 0 and y == 0 and z == 0):
                    outputData.append((x, y, z))
    return outputData

def createTransform4():
    outputData = []
    for x in range(-1,2):
        for y in range(-1,2):
            for z in range(-1,2):
                for w in range(-1,2):
                    if not (x == 0 and y == 0 and z == 0 and w == 0):
                        outputData.append((x, y, z, w))
    return outputData

def valsToCheck(valx,valy,valz,transform):
    outputData = []
    for i in transform:
        outputData.append(((i[0]+valx),(i[1]+valy),(i[2]+valz)))
    return outputData

def valsToCheck4(valx,valy,valz,valw,transform):
    outputData = []
    for i in transform:
        outputData.append(((i[0]+valx),(i[1]+valy),(i[2]+valz),i[3]+valw))
    return outputData

def createInitialData():
    outputData = []
    for y, line in enumerate(dataInput):
        for x, data in enumerate(line):
            if data == '#':
                outputData.append((x,y,0))
    return(outputData)

def createInitialData4():
    outputData = []
    for y, line in enumerate(dataInput):
        for x, data in enumerate(line):
            if data == '#':
                outputData.append((x,y,0,0))
    return(outputData)

def xpos(val):
    return val[0]

def ypos(val):
    return val[1]

def zpos(val):
    return val[2]

def wpos(val):
    return val[3]

def countNeighbor(xval,yval,zval,data,transformData):
    datatocheck = valsToCheck(xval,yval,zval,transformData)
    outputCount = 0
    for i in datatocheck:
        if i in data:
            outputCount += 1
    return outputCount

def countNeighbor4(xval,yval,zval,wval,data,transformData):
    datatocheck = valsToCheck4(xval,yval,zval,wval,transformData)
    outputCount = 0
    for i in datatocheck:
        if i in data:
            outputCount += 1
    return outputCount

def printAxis(data):
    xmax = max(list(map(xpos,(data))))
    xmin = min(list(map(xpos, (data))))
    ymax = max(list(map(ypos, (data))))
    ymin = min(list(map(ypos, (data))))
    zmax = max(list(map(zpos, (data))))
    zmin = min(list(map(zpos, (data))))
    for zcoord in range(zmin, zmax + 1):
        for ycoord in range(ymin, ymax + 1):
            for xcoord in range(xmin, xmax + 1):
                currentCoord = ((xcoord, ycoord, zcoord))
                if currentCoord in data:
                    print('#', end = '')
                else:
                    print('.',end='')
            print('')
        print('')

def main():
    initialData = createInitialData()
    transformData = createTransform()
    datatoCheck = initialData
    for i in range(6):
        tmparray = []
        xmax = max(list(map(xpos, (datatoCheck))))
        xmin = min(list(map(xpos, (datatoCheck))))
        ymax = max(list(map(ypos, (datatoCheck))))
        ymin = min(list(map(ypos, (datatoCheck))))
        zmax = max(list(map(zpos, (datatoCheck))))
        zmin = min(list(map(zpos, (datatoCheck))))
        for xcoord in range(xmin-1,xmax+2):
            for ycoord in range(ymin - 1, ymax + 2):
                for zcoord in range(zmin - 1, zmax + 2):
                    currentCoord = ((xcoord,ycoord,zcoord))
                    neighborCount = countNeighbor(xcoord,ycoord,zcoord,datatoCheck,transformData)
                    if neighborCount == 3:
                        tmparray.append(currentCoord)
                    if neighborCount == 2 and currentCoord in datatoCheck:
                        tmparray.append(currentCoord)
        datatoCheck = tmparray
    return len(datatoCheck)

def main4():
    initialData = createInitialData4()
    transformData = createTransform4()
    datatoCheck = initialData
    for i in range(6):
        loop_time = time.time()
        tmparray = []
        xmax = max(list(map(xpos, (datatoCheck))))
        xmin = min(list(map(xpos, (datatoCheck))))
        ymax = max(list(map(ypos, (datatoCheck))))
        ymin = min(list(map(ypos, (datatoCheck))))
        zmax = max(list(map(zpos, (datatoCheck))))
        zmin = min(list(map(zpos, (datatoCheck))))
        wmax = max(list(map(wpos, (datatoCheck))))
        wmin = min(list(map(wpos, (datatoCheck))))
        for xcoord in range(xmin-1,xmax+2):
            for ycoord in range(ymin - 1, ymax + 2):
                for zcoord in range(zmin - 1, zmax + 2):
                    for wcoord in range(wmin - 1, wmax + 2):
                        currentCoord = ((xcoord,ycoord,zcoord,wcoord))
                        neighborCount = countNeighbor4(xcoord,ycoord,zcoord,wcoord,datatoCheck,transformData)
                        if neighborCount == 3:
                            tmparray.append(currentCoord)
                        if neighborCount == 2 and currentCoord in datatoCheck:
                            tmparray.append(currentCoord)
        datatoCheck = tmparray
        print("Loop",i,"Done in", round(time.time() - loop_time,2),"seconds")
    return len(datatoCheck)

print("Answer 1")
print(main())
print("Answer 2")
print(main4())

"""
Answer 1
395
Answer 2
Loop 0 Done in 0.05 seconds
Loop 1 Done in 0.6 seconds
Loop 2 Done in 2.77 seconds
Loop 3 Done in 20.78 seconds
Loop 4 Done in 28.06 seconds
Loop 5 Done in 179.54 seconds
2296
Took 232.78 seconds to complete
"""

print('Took', round(time.time() - start_time,2), 'seconds to complete')