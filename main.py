import re



#Holding regex code for stuff

guess = 232

#bigregex = re.compile('(byr:)(\S*)(ecl:)(\S*)')
byrtest = re.compile('(byr:)(\S*)')
iyrtest = re.compile('(iyr:)(\S*)')
eyrtest = re.compile('(eyr:)(\S*)')
hgttest = re.compile('(hgt:)(\S*)')
hcltest = re.compile('(hcl:)(\S*)')
ecltest = re.compile('(ecl:)(\S*)')
pidtest = re.compile('(pid:)(\S*)')
cidtest = re.compile('(cid:)(\S*)')
# rex = re.compile('([0-9]+)-([0-9]+) (.): (.+)')
# num1, num2, searchChar, passData = rex.search(x).groups()
# num1 = int(num1)
# num2 = int(num2)


def data():

    count = 0
    dataArray = []
    f = open("/home/daemord/dev/AoC2020/input04.txt", "r")
    #f = open("/home/daemord/dev/AoC2020/input04test.txt", "r")
    #f = open("/home/daemord/dev/AoC2020/input04test02.txt", "r")
    #f = open("/home/daemord/dev/AoC2020/single04.txt", "r")
    fl = f.read().splitlines()
    #put data into array
    byrData1 = ""
    iyrData1 = ""
    eyrData1 = ""
    hgtData1 = ""
    hclData1 = ""
    eclData1 = ""
    pidData1 = ""
    cidData1 = ""
    validTest = 0
    validVerify = 0
    dataentry = 0
    for x in fl:
        if not x:
            tmpArray = [byrData1, iyrData1, eyrData1, hgtData1, hclData1, eclData1, pidData1, cidData1, validTest]
            if validTest == 7:
                validVerify += 1
            dataentry += 1
            print(tmpArray)
            byrData1 = ""
            iyrData1 = ""
            eyrData1 = ""
            hgtData1 = ""
            hclData1 = ""
            eclData1 = ""
            pidData1 = ""
            cidData1 = ""
            validTest = 0
            dataArray.append(tmpArray)

        byrData = byrtest.search(x)
        if byrData:
            byrData1 = byrData.groups()[1]
            byrData1 = int(byrData1)
            if 1920 <= byrData1 <= 2002:
                validTest += 1
            #print(byrData1)
        iyrData = iyrtest.search(x)
        if iyrData:
            iyrData1 = iyrData.groups()[1]
            iyrData1 = int(iyrData1)
            if 2010 <= iyrData1 <= 2020:
                validTest += 1
            #print(iyrData)
        eyrData = eyrtest.search(x)
        if eyrData:
            eyrData1 = eyrData.groups()[1]
            eyrData1 = int(eyrData1)
            if 2020 <= eyrData1 <= 2030:
                validTest += 1
            #print(eyrData)
        hgtData = hgttest.search(x)
        if hgtData:
            hgtData1 = hgtData.groups()[1]
            height, cmin = re.search('([0-9]+)(\S*)',hgtData1).groups()
            height = int(height)
            if cmin == "cm":
                if 150 <= height <= 193:
                    validTest += 1
            elif cmin == "in":
                if 59 <= height <= 76:
                    validTest += 1
            #print(hgtData)
        hclData = hcltest.search(x)
        if hclData:
            hclData1 = hclData.groups()[1]
            hexcode = re.search('(#)(([0-9a-f]){6})',hclData1)
            if hexcode:
                validTest += 1
            #print(hclData)
        eclData = ecltest.search(x)
        if eclData:
            eclData1 = eclData.groups()[1]
            validEye = re.search('(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)',eclData1)
            if validEye:
                validTest += 1
            #print(eclData1)
        pidData = pidtest.search(x)
        if pidData:
            pidData1 = pidData.groups()[1]
            validPid = re.search('^[0-9]{9}$',pidData1)
            if validPid:
                validTest += 1
            #print(pidData)
        cidData = cidtest.search(x)
        if cidData:
            cidData1 = cidData.groups()[1]
            #validTest += 1
            #print(cidData)
    tmpArray = [byrData1, iyrData1, eyrData1, hgtData1, hclData1, eclData1, pidData1, cidData1, validTest]
    if validTest == 7:
        validVerify += 1
    dataentry += 1
    print(tmpArray)
    byrData1 = ""
    iyrData1 = ""
    eyrData1 = ""
    hgtData1 = ""
    hclData1 = ""
    eclData1 = ""
    pidData1 = ""
    cidData1 = ""
    validTest = 0
    dataArray.append(tmpArray)
    #print(dataArray)
    print(validVerify)
    print(dataentry)




data()
