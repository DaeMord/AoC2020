import re
import math
import time
import itertools
from AoC import dataRex
from AoC import printArray
import numpy as np
from collections import defaultdict

start_time = time.time()

#0 Test Short
#1 Actual live data
dataSet = 1

if dataSet == 0:
    dataInput = dataRex('test11.txt','L|.|#')
if dataSet == 1:
    dataInput = dataRex('input11.txt', 'L|.|#')
if dataSet == 2:
    dataInput = dataRex('input112.txt', 'L|.|#')
if dataSet == 3:
    dataInput = dataRex('input113.txt', 'L|.|#')

def emptySeats(inputArray):
    #convert to nparray
    inputArray=np.array(inputArray)
    #reset all seats to empty
    inputArray = np.where(inputArray == 'L', '#', inputArray)
    return inputArray

def addPadding(inputArray):
    y = int(len(inputArray))
    x = int(len(inputArray[0]))
    tmp = ['.'] * (x + 2)
    outPutArray = np.array(tmp)
    for x in inputArray:
        x = np.insert(x, 0, '.')
        x = np.append(x, '.')
        outPutArray = np.vstack([outPutArray, x])
    outPutArray = np.vstack([outPutArray, tmp])
    return outPutArray

def checkSeat(x,y,dataInput):
    xCheck = -1
    yCheck = -1
    filledSeat = 0
    while yCheck < 2:
        while xCheck < 2:
            if dataInput[y+yCheck,x+xCheck] == '#':
                filledSeat += 1
            xCheck += 1
        xCheck = -1
        yCheck += 1
    if dataInput[y,x] == '#':
        filledSeat -= 1
    return filledSeat


def closestSeat(dataInput,splitPoint):
    output = 0
    dataPoint = int(np.where(dataInput == splitPoint)[0])
    dataLeft = np.flip(dataInput[0:dataPoint])
    dataRight = dataInput[dataPoint+1:]
    data2Left = np.where(dataLeft != '.')[0]
    data2Right = np.where(dataRight != '.')[0]
    if data2Left.size != 0 and dataLeft[data2Left][0] == "#":
        output += 1
    if data2Right.size != 0 and dataRight[data2Right][0] == '#':
        output += 1
    return output

def checkSeat2(x,y,dataInput):
    replacementVar = 'C'
    offset = x - y
    calcArray = []
    holddata = ''
    holddata = dataInput[y, x]
    dataInput[y, x] = replacementVar
    # diagonal l>r
    dlr = np.diagonal(dataInput, offset)
    calcArray.append(closestSeat(dlr,replacementVar))
    offset2 = (len(dataInput[0]) - x - 1) - y
    # diagonal r>l
    drl = np.diagonal(np.flip(dataInput, 1), offset2)
    calcArray.append(closestSeat(drl, replacementVar))
    # l>r
    lr = dataInput[y]
    calcArray.append(closestSeat(lr, replacementVar))
    # t>b
    offset3 = (len(dataInput[0]))
    tb = np.rot90(dataInput)[offset3-x-1]
    calcArray.append(closestSeat(tb, replacementVar))
    calcArray = np.array(calcArray)
    calcArray = calcArray.flatten()
    #put original data back in
    dataInput[y,x] = holddata
    return sum(calcArray)


def main(seats):
    testData = addPadding(seats)
    ySeat = 1
    xSeat = 1
    tmp = []
    outPutArray = []
    while ySeat < len(testData) - 1:
        ySeat += 1
        while xSeat < len(testData[0]) - 1:
            xSeat += 1
            seatBeingChecked = testData[ySeat-1,xSeat-1]
            if seatBeingChecked == 'L':
                checkVal = checkSeat(xSeat - 1, ySeat - 1, testData)
                if checkVal == 0:
                    seatBeingChecked = '#'
                else:
                    seatBeingChecked = 'L'
            elif seatBeingChecked == '.':
                seatBeingChecked = '.'
            elif seatBeingChecked == '#':
                checkVal = checkSeat(xSeat - 1, ySeat - 1, testData)
                if checkVal < 4:
                    seatBeingChecked = '#'
                else:
                    seatBeingChecked = 'L'
            tmp.append(seatBeingChecked)
        outPutArray.append(tmp)
        tmp = []
        xSeat = 1
    outPutArray = np.array(outPutArray)
    return outPutArray

def main2(seats):
    testData = addPadding(seats)
    ySeat = 1
    xSeat = 1
    tmp = []
    outPutArray = []
    while ySeat < len(testData) - 1:
        ySeat += 1
        while xSeat < len(testData[0]) - 1:
            xSeat += 1
            seatBeingChecked = testData[ySeat - 1, xSeat - 1]
            checkVal = checkSeat2(xSeat - 1, ySeat - 1, testData)
            if checkVal == 0 and seatBeingChecked == 'L':
                seatBeingChecked = '#'
            if checkVal > 4 and seatBeingChecked == '#':
                seatBeingChecked = 'L'
            tmp.append(seatBeingChecked)
        outPutArray.append(tmp)
        tmp = []
        xSeat = 1
    outPutArray = np.array(outPutArray)
    return outPutArray


def mainLoop(dataInput):
    answerin = np.array(dataInput)
    #answerout = np.array(dataInput)
    answerout = ''
    countloop = 0
    while not np.array_equal(answerin,answerout):
        countloop += 1
        answerout = np.array(answerin)
        answerin = main(answerin)
    return np.count_nonzero(answerin=='#')

def mainLoop2(dataInput):
    answerin = np.array(dataInput)
    #answerout = np.array(dataInput)
    answerout = ''
    countloop = 0
    while not np.array_equal(answerin,answerout):
        countloop += 1
        answerout = np.array(answerin)
        answerin = main2(answerin)
        print("Main Loop",countloop)
    return np.count_nonzero(answerin=='#')



answerin = emptySeats(dataInput)
#testData = addPadding(dataInput)

answer1 = mainLoop(answerin)
answer2 = mainLoop2(answerin)
#answer2 = main2(answerin)


print("Answer 1")
print(answer1)
print("Answer 2")
print(answer2)

print('Took', round(time.time() - start_time,2), 'seconds to complete')