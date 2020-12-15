import time
import re

start_time = time.time()

#0 Test Short
#1 Actual live data
dataSet = 1


if dataSet == 0:
    dataInput = (3, 1, 2)
if dataSet == 1:
    dataInput = (1, 0, 16, 5, 17, 4)


def createInitial():
    output = {}
    for y, i in enumerate(dataInput):
        output[i] = (y+1,y+1)
    return output

def main():
    count = len(dataInput)
    game = createInitial()
    currentCheck = dataInput[-1]

    while True:
        count += 1
        speak = game.get(currentCheck)[0] - game.get(currentCheck)[1]
        if game.get(speak) == None:
            game[speak] = (count,count)
        else:
            game[speak] = (count, game.get(speak)[0])
        currentCheck = speak
        if count == 2020: data1 = speak
        if count == 30000000: return data1, speak

a = main()
print("Answer 1")
print(a[0])
print("Answer 2")
print(a[1])

print('Took', round(time.time() - start_time,2), 'seconds to complete')