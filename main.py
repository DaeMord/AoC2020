import re



#Holding regex code for stuff


# rex = re.compile('([0-9]+)-([0-9]+) (.): (.+)')
# num1, num2, searchChar, passData = rex.search(x).groups()
# num1 = int(num1)
# num2 = int(num2)


def data():

    count = 0
    dataArray = []
    f = open("/home/daemord/dev/AoC2020/input03.txt", "r")
    #f = open("/home/daemord/dev/AoC2020/test03.txt", "r")
    fl = f.read().splitlines()
    #put data into array

    for x in fl:
        count += 1
        holdArray= []
        for y in range(0, len(x)):
            if x[y] == ".":
                tmp = 0
            else:
                tmp = 1
            tmp=int(tmp)
            holdArray.append(tmp)
        dataArray.append(holdArray)

    return(dataArray),count,len(x)

def returnData(xcoord,ycoord,inputdata):
    xcoord = xcoord - 1
    ycoord = ycoord - 1
    return inputdata[xcoord][ycoord]

def treeshitt(treesx,treesy):
    dataInput, sizex, sizey = data()
    startcoordX = 1
    startcoordY = 1
    increasex = treesx
    increasey = treesy
    xCoOrd = startcoordX
    yCoOrd = startcoordY
    treeshit = 0

    while xCoOrd < sizex + 1:
        coordData = returnData(xCoOrd, yCoOrd, dataInput)
        treeshit += coordData
        xCoOrd += increasex
        yCoOrd += increasey
        if yCoOrd > sizey:
            yCoOrd = yCoOrd - sizey

    return treeshit

print(11)
ta=(treeshitt(1,1))
print(ta)
print(13)
tb=(treeshitt(1,3))
print(tb)
print(15)
tc=(treeshitt(1,5))
print(tc)
print(17)
td=(treeshitt(1,7))
print(td)
print(21)
te=(treeshitt(2,1))
print(te)
answer=ta*tb*tc*td*te
print(answer)
