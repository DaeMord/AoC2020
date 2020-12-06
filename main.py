import re
import math


def data():

    answer = 0
    #with open('test06.txt') as f:
    with open('input06.txt') as f:
        lines = f.read().strip()

    dataprocess = lines.split('\n\n')
    #print(dataprocess)
    stripped = [w.replace('\n', '') for w in dataprocess]
    #print(stripped)

    for x in stripped:
        x = "".join(dict.fromkeys(x))
        val = len(x)
        answer += val

    print("Answer 1")
    print(answer)

    prev = ""
    prevdata = ""
    answer2 = 0
    for x in dataprocess:
        for y, ppl in enumerate(x.split('\n')):
            if y == 0:
                tmpcount = (len(ppl))
                prev = ppl
            if y > 0:
                prevdata = get_results(ppl,prev)
                tmpcount = (len(prevdata))
                prev = prevdata
        answer2 += tmpcount
        prev = ""

    print("Answer 2")
    print(answer2)


def get_results(a, b):
    output = ""
    y = ""
    x = list(set([i for i in a+b if a.count(i) == b.count(i)]))
    for y in x:
        output = output + y
    return output


data()
