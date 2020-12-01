# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():

    data = []
    f=open("/home/daemord/dev/AoC2020/input.txt", "r")
    fl =f.readlines()
    for x in fl:
        #print(int(x))
        data.append(int(x))
    print(data)

    #while dpd != 2020:
    for x in data:
        for y in data:
            for z in data:
                dpd=(x+y+z)
                #print(dpd)
                if dpd == 2020:
                    print(x)
                    print(y)
                    print(z)
                    print(x*y*z)
    #print(x)
    #print(y)

if __name__== "__main__":
  main()
