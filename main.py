import time
import re
import copy
from AoC import inputData

start_time = time.time()

#0 Test Short
#1 Actual live data
dataSet = 1

if dataSet == 0:
    dataInput = inputData('test191.txt')
if dataSet == 1:
    dataInput = inputData('test192.txt')
if dataSet == 2:
    dataInput = inputData('input19.txt')

def stripData():
    dataDict = {}
    analysisList = []
    dataType = 0
    for data in dataInput:
        if data == "":
            dataType = 1
        elif dataType == 0:
            lineData,splitData = data.split(': ')
            if splitData.startswith('"'):
                dataDict[int(lineData)] = eval(splitData)
            else:
                dataDict[int(lineData)] = [[*map(int, part.split())] for part in splitData.split(' | ')]
        elif dataType == 1:
            analysisList.append(data)
    return dataDict,analysisList


data = stripData()[0]

def buildReg(idx):
    val0 = (data[idx])
    if isinstance(val0,str):
        return val0
    if len(val0) == 2:
        outputArray = []
        for i in val0:
            array1 = ""
            array2 = []
            for z in i:
                if isinstance(buildReg(z),str):
                    array1 = array1 + buildReg(z)
                else:
                    array2.append(buildReg(z))
            if len(array2) == 0:
                outputArray.append(array1)
            else:
                outputArray = array2
        return(outputArray)

for i in (data[0][0]):
    x = buildReg(i)
    if isinstance(x,str):
        print(x)
    else:
        for i in x:
            print(i)


print("Answer 1")
#print(main(dataInput1,1))
print("Answer 2")
#print(main(dataInput2,2))


print('Took', round(time.time() - start_time,2), 'seconds to complete')