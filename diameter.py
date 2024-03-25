#ass4 Task 1
#size = number of arcs
import sys
import math

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
            result.append(get_diameter(info, order))
            info = []
            
            order = int(infolist[i])
            count = order
            
    return result

def get_diameter(infolist, order):
    result = []
    count = []
    for i in range(len(infolist)):
        result.append(visit([i, infolist, order]))

    for i in range(len(result)):
        for n in range(len(result[i])):
            if (result[i][n] == 0 and i != n):
                result[i][n] = 90000

    for i in range(len(result)):
        count.append(max(result[i]))
    return max(count)

def visit(everything):
    queue = []
    node = everything[0]
    edges = everything[1]
    order = everything[2]
    steps = [0] * order
    colour = ["W"] * order

    colour[node] = "G"
    queue.append(node)
    while len(queue) != 0:
        u = queue[0]
        for out in range(len(edges[u])):
            nextnode = int(edges[u][out])
            if colour[nextnode] == "W":
                colour[nextnode] = "G"
                queue.append(nextnode)
                steps[nextnode] = steps[u]+1

        queue = queue[1:]
        colour[u] = "B"
    return steps


info = []

for line in sys.stdin:
    info.append(line.strip())

d = seperate(info)
for i in range(len(d)):
    if d[i] == 90000:
        print("Graph {} is disconnected.".format(i+1))
    else:
        print("Graph {} has diameter {}.".format(i+1, d[i]))


