import time
import re
import copy
from AoC import inputData

start_time = time.time()

#0 Test Short
#1 Actual live data
dataSet = 1
#test data = 71, 26, 437, 12240, 13632

if dataSet == 0:
    dataInput = inputData('test18.txt',t="rfa",r='(\d|\+|\*|\(|\))')
if dataSet == 1:
    dataInput = inputData('input18.txt',t="rfa",r='(\d|\+|\*|\(|\))')

def performMath(data):
    val1 = int(data[0])
    for i in range(0,len(data)-1,2):
        val2 = int(data[i+2])
        if (data[i+1]) == '+':
            val0 = val1 + val2
        if (data[i+1]) == '*':
            val0 = val1 * val2
        val1 = val0
    return val1

def performMath2(data):
    while data.count('+') > 0:
        multi = data.index('+')
        datatoInsert = int(data[multi-1]) + int(data[multi+1])
        del(data[multi-1:multi+2])
        data.insert(multi-1,datatoInsert)
    while data.count('*') > 0:
        multi = data.index('*')
        datatoInsert = int(data[multi-1]) * int(data[multi+1])
        del(data[multi-1:multi+2])
        data.insert(multi-1,datatoInsert)
    return (int(data[0]))

def main(dataData,part):
    runningTotal = 0
    for data in dataData:
        while data.count(')') > 0:
            closeBracket = data.index(')')
            arrayToBracket = data[0:closeBracket]
            arrayReverse = arrayToBracket[::-1]
            openBracket = arrayReverse.index('(')
            arraytoOpenBracket = arrayReverse[0:openBracket]
            backtoNormal = arraytoOpenBracket[::-1]
            if part == 1:
                valToInsert = performMath(backtoNormal)
            else:
                valToInsert = performMath2(backtoNormal)
            del(data[closeBracket-openBracket-1:closeBracket+1])
            data.insert(closeBracket-openBracket-1,valToInsert)
        if part == 1:
            answer = performMath(data)
        else:
            answer = performMath2(data)
        runningTotal += answer
    return runningTotal

dataInput1 = copy.deepcopy(dataInput)
dataInput2 = copy.deepcopy(dataInput)

print("Answer 1")
print(main(dataInput1,1))
print("Answer 2")
print(main(dataInput2,2))


print('Took', round(time.time() - start_time,2), 'seconds to complete')