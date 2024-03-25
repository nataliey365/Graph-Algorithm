import sys

def seperate(infolist):
    result = []
    info = []
    order = int(infolist[0])
    count = order

    for i in range(1, len(infolist)):
        if count != 0:
            info.append(infolist[i].split())
            count -= 1
        else:
            matrix(info, order)
            info = []
            order = int(infolist[i])
            count = order
    print(0)
            
    return result

def matrix(infolist, order):
    print(order)
    line = ["0"] * order

    for i in range(order):
        for val in range(len(infolist[i])):
            line[int(infolist[i][val])] = "1"
        joined = " ".join(line)
        joined += " "
        print(joined)
        line = ["0"] * order
    return 
                


info = []
result = []
for line in sys.stdin:
    info.append(line.strip())

seperate(info)