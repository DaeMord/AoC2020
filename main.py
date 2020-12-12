import time
from AoC import dataRex
from AoC import rotate

start_time = time.time()

#0 Test Short
#1 Actual live data
dataSet = 1

if dataSet == 0:
    dataInput = dataRex('test12.txt','([A-Z])(\d*)')
if dataSet == 1:
    dataInput = dataRex('input12.txt', '([A-Z])(\d*)')

def main():
    currentDir = 'E'
    currentDirVal = 0
    dirlist= ['E', 'S', 'W', 'N']
    countN = 0
    countS = 0
    countW = 0
    countE = 0
    for i in dataInput:
        if i[0] == 'R':
            currentDirVal = currentDirVal + round(int(i[1])/90)
            if currentDirVal > 3: currentDirVal -= 4
            currentDir = dirlist[currentDirVal]
        if i[0] == 'L':
            currentDirVal = currentDirVal - round(int(i[1]) / 90)
            if currentDirVal < 0: currentDirVal += 4
            currentDir = dirlist[currentDirVal]
        if i[0] == 'F':
            testVal = currentDir
        else:
            testVal = i[0]
        if testVal == 'N':
            countN += int(i[1])
        if testVal == 'S':
            countS += int(i[1])
        if testVal == 'W':
            countW += int(i[1])
        if testVal == 'E':
            countE += int(i[1])

    NS = abs(countN-countS)
    EW = abs(countE-countW)
    output = NS + EW
    return output

def main2():
    wayPoint = [1, 10]
    currentCoOrd = [0, 0]

    for i in dataInput:
        if i[0] == 'R':
            rotVal = rotate((0, 0), (wayPoint[1], wayPoint[0]), int(i[1]) * -1)
            wayPoint[0], wayPoint[1] = rotVal[1], rotVal[0]
        elif i[0] == 'L':
            rotVal = rotate((0, 0), (wayPoint[1], wayPoint[0]), int(i[1]))
            wayPoint[0], wayPoint[1] = rotVal[1], rotVal[0]
        elif i[0] == 'F':
            currentCoOrd[0] = currentCoOrd[0] + (wayPoint[0] * int(i[1]))
            currentCoOrd[1] = currentCoOrd[1] + (wayPoint[1] * int(i[1]))
        elif i[0] == 'N':
            wayPoint[0] = wayPoint[0] + int(i[1])
        elif i[0] == 'S':
            wayPoint[0] = wayPoint[0] - int(i[1])
        elif i[0] == 'W':
            wayPoint[1] = wayPoint[1] - int(i[1])
        elif i[0] == 'E':
            wayPoint[1] = wayPoint[1] + int(i[1])
    output = abs(currentCoOrd[0]) + abs(currentCoOrd[1])
    return output


print("Answer 1")
print(main())
print("Answer 2")
print(main2())

print('Took', round(time.time() - start_time,2), 'seconds to complete')