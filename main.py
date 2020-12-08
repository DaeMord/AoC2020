import re
import math
import time
start_time = time.time()

rex = re.compile('(...)\s(.)(\d*)')

def data():

    #with open('test08.txt') as f:
    with open('input08.txt') as f:
        lines = f.read().strip()

    dataprocess = lines.split('\n')
    stripped = [w.replace('\n', '') for w in dataprocess]
    dataoutput = []
    for x in stripped:
        data = list(rex.search(x).groups())
        dataoutput.append(data)
    return dataoutput

def arraysrc(data,src):
    output = []
    for y, i in enumerate(data):
        if i[0] == src:
            output.append(y)
    return output

def analyse(data):
    i = 0
    acc = 0
    entrydone = [0]
    while i < len(data):
        if data[i][0] == "nop":
            i += 1
        elif data[i][0] == "jmp":
            if data[i][1] == "+":
                i = i + (int(data[i][2]))
            elif data[i][1] == "-":
                i = i - (int(data[i][2]))
        elif data[i][0] == "acc":
            if data[i][1] == "+":
                acc += int(data[i][2])
                i += 1
            elif data[i][1] == "-":
                acc -= int(data[i][2])
                i += 1
        if i not in entrydone:
            entrydone.append(i)
        else:
            break
    return(acc,i,len(data))

def swptest(var1,var2):
    datainput = data()
    datahold = []
    for i in arraysrc(datainput,var1):
        datahold = datainput
        datahold[i][0] = var2
        x = analyse(datahold)
        datahold[i][0] = var1
        if (x[1]) == (x[2]):
            return(i,x[0])

answer1 = analyse(data())
jmp = (swptest("jmp","nop"))
#nop = (swptest("nop","jmp"))
print("Answer 1")
print(answer1[0])
print("Answer 2")
print(jmp[1])

print('Took', time.time() - start_time, 's to complete')