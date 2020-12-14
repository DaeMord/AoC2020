import time
import re
from AoC import inputData

start_time = time.time()

#0 Test Short
#1 Actual live data
dataSet = 1

# 3459377600572 not answer

if dataSet == 0:
    dataInput = inputData('test14.txt')
if dataSet == 1:
    dataInput = inputData('input14.txt')
if dataSet == 2:
    dataInput = ['mask = 000000000000000000000000000000X1001X', 'mem[42] = 100']
if dataSet == 3:
    dataInput = inputData('test142.txt')
if dataSet == 4:
    dataInput = inputData('test143.txt')
if dataSet == 5:
    #dataInput = ['mask = X00X0100100X111X01001X10X001X00X0100', 'mem[363] = 58081970', 'mem[35105] = 31435010', 'mem[52446] = 4898641']
    dataInput = ['mask = X00X0100100X111X01001X10X001X00X0100', 'mem[363] = 58081970']

def maskData(mask):
    output = []
    for y, i in enumerate(mask [::-1]):
        if i != 'X':
            output.append((y,int(i)))
    return output

def merge(binary, mask):
    binaryDict = dict(binary)
    maskDict = dict(mask)
    maxNum = binary + mask
    maxNum = (max(map(max, maxNum)))
    output = ''
    for i in range(maxNum+1):
        if maskDict.get(i) == None:
            if binaryDict.get(i) == None:
                output = output + '0'
            else:
                output = output + str(binaryDict.get(i))
        else:
            output = output + str(maskDict.get(i))
    return output

def merge2(binary, mask):
    binaryDict = dict(binary)
    maskDict = dict(mask)
    output = []
    maskcheck = ""
    for i in range(36):
        if maskDict.get(i) == None:
            maskcheck = maskcheck + 'X'
            if len(output) == 0:
                output.append('0')
                output.append('1')
            else:
                string0 = '0'
                string1 = '1'
                var0 = [x + string0 for x in output]
                var1 = [x + string1 for x in output]
                output = var0 + var1
        else:
            if maskDict.get(i) == 0:
                maskcheck = maskcheck + '0'
                if binaryDict.get(i) == None:
                    string0 = '0'
                else:
                    string0 = str(binaryDict.get(i))
            else:
                maskcheck = maskcheck + '1'
                string0 = '1'
            if len(output) == 0:
                output.append(string0)
            else:
                var0 = [x + string0 for x in output]
                output = var0
    actOutput = []
    for i in output:
        intOutput = int(i [::-1], base = 2)
        actOutput.append(intOutput)
    return actOutput

def main():
    memSize = 0
    for data in dataInput:
        if "mem" in data:
            mem = re.search('mem[[](\d*)[]] = (\d*)', data).groups()
            if int(mem[0]) > memSize:
                memSize = int(mem[0])
    #intitialise memory array
    memArray1 = {}
    memArray2 = {}
    for data in dataInput:
        if "mask" in data:
            mask = re.search('mask = (\S*)',data)[1]
            maskD = maskData(mask)
        elif "mem" in data:
            mem = re.search('mem[[](\d*)[]] = (\d*)',data).groups()
            binaryMem = bin(int(mem[0]))
            binary = bin(int(mem[1]))
            binary = binary [::-1]
            binaryMem = binaryMem[::-1]
            binary = binary[:-2]
            binaryMem = binaryMem[:-2]
            binary = binary [::-1]
            binaryMem = binaryMem[::-1]
            binary = maskData(binary)
            binaryMem = maskData(binaryMem)
            finalBinary = merge(binary,maskD)
            memAssign = merge2(binaryMem,maskD)
            finalBinary = finalBinary [::-1]
            val = int(finalBinary,base=2)
            for i in memAssign:
                memArray2[i] = int(mem[1])
            memArray1[int(mem[0])-1] = val
    return sum(memArray1.values()),sum(memArray2.values())

print("Answer 1")
print(main()[0])
print("Answer 2")
answer2 = main()[1]
if answer2 == 3459377600572:
    print("Run it again")
print(answer2)

print('Took', round(time.time() - start_time,2), 'seconds to complete')