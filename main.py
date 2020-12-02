import re


def main():

    f = open("/home/daemord/dev/AoC2020/input02.txt", "r")
    fl = f.readlines()
    passfound = 0
    passfound2 = 0
    for x in fl:
        rex = re.compile('([0-9]+)-([0-9]+) (.): (.+)')
        num1, num2, searchChar, passData = rex.search(x).groups()
        num1 = int(num1)
        num2 = int(num2)
        if passData.count(searchChar) <= num2:
            if passData.count(searchChar) >= num1:
                passfound = passfound + 1

        if passData[num1-1] == searchChar or passData[num2-1] == searchChar:
            data1 = passData[num1-1]
            data2 = passData[num2-1]
            data3 = data1 + data2
            print(data3)
            countString = data3.count(searchChar)
            print(searchChar)
            print(countString)
            if countString == 1:
                passfound2 = passfound2 + 1
    print(passfound)
    print(passfound2)

if __name__== "__main__":
  main()
