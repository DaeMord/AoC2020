import re
import math
import time
import itertools

start_time = time.time()

#0 Test Short
#1 Test Long
#2 Actual live data
dataInput = 2

def datat():

    dataoutput = []
    fileName = ''
    fileName = 'test10f.txt'
    with open(fileName) as f:
        for line in f:
            linedata = line.strip()
            data = linedata
            dataoutput.append(int(data))
    #dataoutput.append(0)

    return dataoutput

def data():

    dataoutput = []
    fileName = ''
    if dataInput == 0: fileName = 'test10s.txt'
    if dataInput == 1: fileName = 'test10l.txt'
    if dataInput == 2: fileName = 'input10.txt'
    if dataInput == 3: fileName = 'test10f.txt'
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
    dataCheck = sorted(data)
    complete_list = list(set(dataCheck)) + [dataCheck[-1] + 3]
    times = 1
    left, right = 0, 0
    while left < len(complete_list) - 1 and right < len(complete_list) - 1:
        while complete_list[right + 1] - complete_list[right] == 1:
            right += 1
        times *= count_combination(complete_list[left:right+1])
        right += 1
        left = right
    return times

def count_combination(adapters):
    if len(adapters) == 3:
        return 2
    elif len(adapters) > 3:
        # full list + (full list minus 1 of the middle numbers) + (full list minus combination of any 2 middle numbers)
        result = 1 + len(adapters) - 2 + int(math.factorial(len(adapters) - 2) / 2)
        return result
    return 1

def canIRemove(dataPosition,data):
    datal = data[dataPosition[0]-1]
    if dataPosition[1]+1 == len(data):
        datah = data[dataPosition[1]]+3
    else:
        datah = data[dataPosition[1]+1]
    if datah-datal < 4:
        return True
    return False


def countSomething():
    data = datat()
    flat = list(itertools.combinations(data,1))
    numbers = list(itertools.combinations(data, 2))
    numbers1 = list(itertools.combinations(data, 3))
    numbers2 = list(itertools.combinations(data, 4))
    numbers3 = list(itertools.combinations(data, 5))
    print(flat)
    print(numbers)
    print(numbers1)
    print(numbers2)
    print(numbers3)
    print(len(flat))
    print(len(numbers))
    print(len(numbers1))
    print(len(numbers2))
    print(len(numbers3))


dataInput = data()
#countSomething()
dataOutput = analyse(dataInput)
answer1 = dataOutput[1] * dataOutput[3]
answer2 = analyse2(dataInput)
print("Answer 1")
print(answer1)
print("Answer 2")
print(answer2)

print('Took', round(time.time() - start_time,2), 'seconds to complete')