import re
import math
import time
import itertools

start_time = time.time()

#0 Test Short
#1 Test Long
#2 Actual live data
dataInput = 2

def data():

    dataoutput = []
    fileName = ''
    if dataInput == 0: fileName = 'test10s.txt'
    if dataInput == 1: fileName = 'test10l.txt'
    if dataInput == 2: fileName = 'input10.txt'
    with open(fileName) as f:
        for line in f:
            linedata = line.strip()
            data = linedata
            dataoutput.append(int(data))
    dataoutput.append(0)

    return dataoutput


def difInArray(input,data):
    #Returns (difference in array), (output value)
    # -1,-1 if not found
    i = 0
    while i < 3:
        i += 1
        if input + i in data:
            return(i, input + i)
    return -1,-1

def compareArray(A, B):
    #return ', '.join(map(str, A)) in ', '.join(map(str, B))
    n = len(A)
    return any(A == B[i:i + n] for i in range(len(B)-n + 1))

def analyse(data):
    currentVal = 0
    countArray = []
    while currentVal < max(data):
        activeData = difInArray(currentVal, data)
        if activeData[0] == -1: return -1, -1, -1, -1
        currentVal = activeData[1]
        countArray.append(activeData[0])
    #add final value for output
    currentVal = currentVal + 3
    countArray.append(3)
    #do a count on 1/2/3
    c1 = countArray.count(1)
    c2 = countArray.count(2)
    c3 = countArray.count(3)
    return currentVal, c1, c2, c3


def analyse2(data):
    loopcount = 0
    i = 1
    dataCheck = sorted(data)
    whereChange = []
    while i < len(data):
        x = canIRemove((i, i), dataCheck)
        if x:
            whereChange.append(i)
        i += 1
    print(whereChange)
    print(len(whereChange)+1)


def canIRemove(dataPosition,data):
    datal = data[dataPosition[0]-1]
    if dataPosition[1]+1 == len(data):
        datah = data[dataPosition[1]]+3
    else:
        datah = data[dataPosition[1]+1]
    if datah-datal < 4:
        return True
    return False

dataInput = data()
dataOutput = analyse(dataInput)
answer1 = dataOutput[1] * dataOutput[3]
analyse2(dataInput)
print("Answer 1")
print(answer1)
print("Answer 2")
#print(answer2)

print('Took', round(time.time() - start_time,2), 'seconds to complete')