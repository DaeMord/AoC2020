import time
import re
from AoC import rotate
from AoC import inputData

start_time = time.time()

#0 Test Short
#1 Actual live data
dataSet = 1

if dataSet == 0:
    dataInput = inputData('test13.txt')
if dataSet == 1:
    dataInput = inputData('input13.txt')

def main():
    busDepart = int(dataInput[0])
    busTimes = dataInput[1].split(',')
    dataBusTimesOriginal = []
    dataBusTimesOutput = []
    for i in busTimes:
        if i != 'x':
            dataBusTimesOriginal.append(int(i))
            dataBusTimesOutput.append(int(i))
    while min(dataBusTimesOutput) < busDepart:
            minIndex = dataBusTimesOutput.index(min(dataBusTimesOutput))
            dataBusTimesOutput[minIndex] = dataBusTimesOutput[minIndex] + dataBusTimesOriginal[minIndex]
    minIndex = dataBusTimesOutput.index(min(dataBusTimesOutput))
    return dataBusTimesOriginal[minIndex]*(dataBusTimesOutput[minIndex]-busDepart)

def main2():
    busDepart = int(dataInput[0])
    busTimes = dataInput[1].split(',')
    dataBusTimesOriginal = []
    dataBusTimesOutput = []
    diffIndex = []
    countx = 1
    for i in busTimes:
        if i != 'x':
            dataBusTimesOriginal.append(int(i))
            dataBusTimesOutput.append(int(i))
            diffIndex.append(int(countx))
            countx = 1
        elif i == 'x':
            countx += 1
    diffIndex.pop(0)
    return function(dataBusTimesOriginal, diffIndex)

def checkIfValid(val1, val2, diff):
    origVal1 = val1
    while True:
        while (val1+diff) % val2 != 0:
            val1 += origVal1
        yield val1
        val1 += origVal1

def itterate(num1,num2,diffnum,reachNumber):
    x = checkIfValid(num1, num2, diffnum)
    while True:
        y = next(x)
        if y == reachNumber:
            return y
        if y > reachNumber:
            return -1

def function(array1, array2):
    x = checkIfValid(array1[0], array1[-1], sum(array2))
    i = -1
    while True:
        i += 1
        numtocheck = next(x)
        result = 0
        y = -1
        while result != -1:
            y += 1
            result = itterate(array1[y],array1[y+1],array2[y],numtocheck+sum(array2[:y]))
            if y == len(array1)-2: break
        if result > 0:
            return numtocheck

print("Answer 1")
print(main())
print("Answer 2")
print(main2())

print('Took', round(time.time() - start_time,2), 'seconds to complete')