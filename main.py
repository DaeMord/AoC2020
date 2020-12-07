import re
import math
import time
start_time = time.time()

rex = re.compile('(^(.*?)bag)|(contain [0-9] ((.*?)bag))|(, [0-9] ((.*?)bag))')
rex2 = re.compile('(\w* \w*) (bag)')
rex3 = re.compile('\d')

def data():

    #with open('test07.txt') as f:
    with open('input07.txt') as f:
    #with open('test0702.txt') as f:
        lines = f.read().strip()

    #dataprocess = lines.split('\n\n')
    dataprocess = lines.split('\n')
    stripped = [w.replace('\n', '') for w in dataprocess]
    return stripped


def bagcount(srch,datainput):
    count = 0
    countnew = 0
    for x in datainput:
        data = rex2.findall(x)
        for i in data:
            if i[0] == srch:
                if data[0][0] == srch:
                    if data[0][0] not in bagcan:
                        bagcan.append(data[0][0])
                else:
                    if data[0][0] not in srchfor:
                        srchfor.append(data[0][0])
                        bagcount(data[0][0],datainput)

    count = len([i for i in bagcan if i != srch])
    return count

def bagcount2(srch,countinput, datainput):
    count = 0
    countnew = 0
    if countinput == 0:
        countinput = 1
    runningttl = 0
    for x in datainput:
        data = rex2.findall(x)
        if data[0][0] == srch:
            for i in bagcountnew(srch)[1:]:
                newfigure = i[1]
                cnt = bagcount2(i[0],newfigure, datainput)
                if cnt == 0:
                    runningttl += newfigure
                else:
                    runningttl += cnt

    count = runningttl * countinput + countinput
    return count

def bagdata(datainput):
    output = []
    for x in datainput:
        tmp = []
        data = rex2.findall(x)
        tmp.append(data[0][0])
        data2 = rex3.findall(x)
        for i in data[1:]:
            val = 0
            for i in data2:
                val += int(i)
        tmp.append(val)
        for y, i in enumerate(data[1:]):
            tmp.append(i[0])
            if (i[0]) != "no other":
                tmp.append(data2[y])
            val = 0
            for i in data2:
                val += int(i)
        output.append(tmp)
    return output

def bagcountnew(srch):
    output = []
    for x in bagdata(data()):
        if x[0] == srch:
            output.append(x[1])
            for y, i in enumerate(x[2:]):
                if (y % 2) == 0:
                    tmp = []
                    tmp.append(i)
                else:
                    tmp.append(int(i))
                    output.append(tmp)
    return output

srchfor = []
bagcan = []
answer1 = bagcount("shiny gold",data())
answer2 = bagcount2("shiny gold",1,data()) - 1
#answer2 = bagdata(data())
#print(bagcountnew("shiny gold"))

print("Answer 1")
print(answer1)
print("Answer 2")
print(answer2)

print('Took', time.time() - start_time, 's to complete')

