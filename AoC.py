import re
import math

def test():
    print("Test")


def dataStr(filename):

    dataoutput = []
    fileName = filename
    with open(fileName) as f:
        for line in f:
            linedata = line.strip()
            data = linedata
            dataoutput.append(data)

    return dataoutput

def dataInt(filename):

    dataoutput = []
    fileName = filename
    with open(fileName) as f:
        for line in f:
            linedata = line.strip()
            data = linedata
            dataoutput.append(int(data))

    return dataoutput

def dataRex(filename,rex):

    regex = re.compile(rex)
    dataoutput = []
    fileName = filename
    with open(fileName) as f:
        for line in f:
            linedata = line.strip()
            data = regex.search(linedata).groups()
            dataoutput.append(data)
    return dataoutput

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point
    angle = math.radians(angle)

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return round(qx), round(qy)

def printArray(inputArray):
    for x in inputArray:
        for y in x:
            print(y,end='')
        print()
