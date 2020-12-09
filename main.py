import re
import math
import time
import itertools
start_time = time.time()

rex = re.compile('(...)\s(.)(\d*)')

def data():

    dataoutput = []
    #with open('test09.txt') as f:
    with open('input09.txt') as f:
        for line in f:
            linedata = line.strip()
            data = linedata
            dataoutput.append(int(data))

    return dataoutput

def somedata(data,varWide):
    for loopValue, a in enumerate(data):
        val = data[loopValue+varWide]
        if val not in [sum(numbers) for numbers in itertools.combinations(data[loopValue:loopValue+varWide],2)]: return(val)

def analyse(data,range):
    invalid = []
    for loopValue, a in enumerate(data):
        checkValue = loopValue + range
        dataTest = data[loopValue:checkValue]
        dataToCheck = data[checkValue]
        arrayToBeChecked = []
        for i in dataTest:
            for j in dataTest:
                tmp = i + j
                arrayToBeChecked.append(tmp)
        if dataToCheck not in arrayToBeChecked:
            invalid.append(dataToCheck)
        if loopValue >= (len(data) - range - 1): break
    return invalid[0]

def analyse2(data,valueToFind):
    i = 1
    output = 0
    for loopValue, a in enumerate(data):
        while i < len(data):
            dataSum = sum(data[loopValue:i])
            if dataSum == valueToFind:
                answerArray = data[loopValue:i]
                if len(answerArray) > 1:
                    output = min(answerArray) + max(answerArray)
            if dataSum > valueToFind: break
            i += 1
        i = loopValue + 2
    return output


wide = 25
dataInput = data()
answer1 = analyse(dataInput,wide)
answer2 = analyse2(dataInput,answer1)
print(somedata(dataInput,wide))
print("Answer 1")
print(answer1)
print("Answer 2")
print(answer2)

print('Took', round(time.time() - start_time,2), 'seconds to complete')