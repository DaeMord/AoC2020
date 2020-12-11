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

    dataoutput = []
    fileName = filename
    with open(fileName) as f:
        for line in f:
            linedata = line.strip()
            data = linedata
            dataoutput.append(int(data))

    return dataoutput