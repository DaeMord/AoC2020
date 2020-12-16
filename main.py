import time
import re
from AoC import inputData

start_time = time.time()

#0 Test Short
#1 Actual live data
dataSet = 1


if dataSet == 0:
    dataInput = inputData('test16.txt')
if dataSet == 1:
    dataInput = inputData('input16.txt')
if dataSet == 2:
    dataInput = inputData('test162.txt')

def checkData():
    entryrex = re.compile('^(.*): (\d*)-(\d*) or (\d*)-(\d*)')
    checkDataDict = {}
    dataType = 0
    yourTicket = []
    closeTickets = []
    for y, i in enumerate(dataInput):
        if i == '':
                pass
        elif i == 'your ticket:':
            dataType = 1
        elif i == 'nearby tickets:':
            dataType = 2
        else:
            if dataType == 0:
                dataLine = entryrex.search(i).groups()
                checkDataDict[dataLine[0]] = ((int(dataLine[1]) , int(dataLine[2])),(int(dataLine[3]),int(dataLine[4])))
            elif dataType == 1:
                yourTicket = i.split(',')
            elif dataType == 2:
                tmpTicket = i.split(',')
                closeTickets.append(tmpTicket)
    return checkDataDict, yourTicket, closeTickets

def createRangeData(checkDict):
    rangeData = []
    locationDict = {}
    y = 0
    for i in checkDict:
        rangeData.append(checkDict[i][0])
        rangeData.append(checkDict[i][1])
        locationDict[y] = i
        locationDict[y+1] = i
        y += 2
    return rangeData,locationDict

def main(data):
    rangeDataReturn = createRangeData(data[0])
    rangeData = rangeDataReturn[0]
    outofRange = []
    validTicket = []
    ticketData = data[2]
    for i in ticketData:
        ticketInvalid = 0
        for y in i:
            inRange = 0
            for z in rangeData:
                if z[0] <= int(y) <= z[1]:
                    inRange = 1
            if inRange == 0:
                outofRange.append(int(y))
                ticketInvalid = 1
        if ticketInvalid == 0: validTicket.append(i)
    return sum(outofRange),validTicket

def findRowAnswer(validTickets,data,column):
    rangeData = data[0]
    dictCheck = data[1]
    val1 = set()
    for i in validTickets:
        val0 = set()
        for d, z in enumerate(rangeData):
            if z[0] <= int(i[column]) <= z[1]:
                val0.add(dictCheck[d])
        #print(val0,val1)
        commonValue = val0.intersection(val1)
        #print(commonValue)
        val1 = set()
        if len(commonValue) > 0:
            val1 = commonValue
        else:
            val1 = val0
    return commonValue

data = checkData()
rangeData = createRangeData(data[0])
output = main(data)
findRow = findRowAnswer(output[1],rangeData,0)
ticketInfo = []
for i in range(len(output[1][0])):
    findRow = findRowAnswer(output[1], rangeData, i)
    ticketInfo.append(list(findRow))
dictTicketInfo = {}
setFound = set()
loop = 0
while True:
    loop += 1
    arraycount = 0
    for y, i in enumerate(ticketInfo):
        if len(i) == 1:
            dictTicketInfo[y] = i[0]
            setFound.add(i[0])
    for y, i in enumerate(ticketInfo):
        if len(i) > 1:
            ticketInfo[y] = (list(set(ticketInfo[y]) - setFound))
        else:
            arraycount += 1
    if arraycount == 20: break
finalOutput = 1
for y, i in enumerate(ticketInfo):
    if re.search('^departure', i[0]):
        finalOutput *= int(data[1][y])

print("Answer 1")
print(output[0])
print("Answer 2")
print(finalOutput)

print('Took', round(time.time() - start_time,2), 'seconds to complete')