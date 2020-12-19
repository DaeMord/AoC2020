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
            lineData = data.replace(':','').replace('"','').split()
            dataDict[int(lineData[0])] = lineData[1:]
        elif dataType == 1:
            analysisList.append(data)
    return dataDict,analysisList

def findVals(data,val):
    dataOutput = []
    for i in val:
        for y in data[i]:
            if (y) != '|':
                if len(data[int(y)]) == 1:
                    if len(dataOutput) == 0:
                        dataOutput.append(data[int(y)][0])
                    else:
                        tmp = []
                        for z, x in enumerate(dataOutput):
                            tmp.append(x+data[int(y)][0])
                        dataOutput = tmp
                else:
                    dataOutput.append(findVals(data,[int(y)]))

            else:
                tmp = []
                print("Doing This")
                print(dataOutput)
                for x in dataOutput:
                    tmp.append(x + '|')
                dataOutput = tmp
    if len(dataOutput) == 1:
        #print(dataOutput[0].split('|'))
        pass
    else:
        #print(dataOutput)
        pass
    #print(tmpnew)
    #return dataOutput[0].split('|')

data = stripData()[0]
print(findVals(data,[1]))

print("Answer 1")
#print(main(dataInput1,1))
print("Answer 2")
#print(main(dataInput2,2))


print('Took', round(time.time() - start_time,2), 'seconds to complete')