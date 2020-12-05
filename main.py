import re
import math



#Holding regex code for stuff

# rex = re.compile('([0-9]+)-([0-9]+) (.): (.+)')
# num1, num2, searchChar, passData = rex.search(x).groups()
# num1 = int(num1)
# num2 = int(num2)


def data():

    seat = []
    count = 0
    f = open("/home/daemord/dev/AoC2020/input05.txt", "r")
    #f = open("/home/daemord/dev/AoC2020/test05.txt", "r")
    #f = open("/home/daemord/dev/AoC2020/single05.txt", "r")
    fl = f.read().splitlines()
    lowvalr=0
    hivalr=127
    lowvalc=0
    hivalc=7
    hianswer = 0

    for x in fl:
        count += 1
        lowvalr = 0
        hivalr = 127
        lowvalc = 0
        hivalc = 7
        for y in range(0, len(x)):
            if y <= 6:
                val1 = process(x[y],lowvalr,hivalr)
                lowvalr = val1[0]
                hivalr = val1[1]
                if lowvalr == hivalr:
                    answerr = lowvalr
            if y > 6:
                val1 = process(x[y], lowvalc, hivalc)
                lowvalc = val1[0]
                hivalc = val1[1]
                if lowvalc == hivalc:
                    answerc = lowvalc
        #print(x)
        #print(answerr)
        #print(answerc)
        answer = (answerr * 8) + answerc
        if answer > hianswer:
            hianswer = answer
        seat.append(answer)
        #print(answer)
    print(hianswer)
    list.sort(seat)
    seattest = seat[0] - 1
    #print(seattest)
    for x in seat:
        if seattest + 1 != x:
            print(x-1)
            seattest = x
        else:
            seattest = x
    #print(seat)
    #print(count)



def process(inputchar,lower,upper):
    if inputchar == "B":
        outputl = upper - lower
        outputl = math.floor(outputl / 2)
        outputl = lower + (outputl + 1)
        outputh = upper
    if inputchar == "F":
        outputl = lower
        outputh = upper - lower
        outputh = math.floor(outputh / 2)
        outputh = upper - (outputh + 1)
    if inputchar == "R":
        outputl = upper - lower
        outputl = math.floor(outputl / 2)
        outputl = lower + (outputl + 1)
        outputh = upper
    if inputchar == "L":
        outputl = lower
        outputh = upper - lower
        outputh = math.floor(outputh / 2)
        outputh = upper - (outputh + 1)
    return(outputl, outputh)




data()
