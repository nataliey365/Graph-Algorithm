#ass4 Task 1
#size = number of arcs
import sys
import math

def seperate(infolist):
    result = []
    info = []
    order = int(infolist[0])
    count = order
    sizes = []

    for i in range(1, len(infolist)):
        if count != 0:
            info.append(infolist[i].split())
            count -= 1
        else:
            sizes.append(get_size(info, order))
            info = []
            
            order = int(infolist[i])
            count = order
            
    return sizes

def get_size(infolist, order):
    colour = []
    pred = []
    steps = [0] * order
    
    size = 0
    for i in range(len(infolist)):
        colour.append("W")
        pred.append("")

    for i in range(len(infolist)):
        if colour[i] == "W":
            count = visit([i, infolist, colour, pred, steps])
            size += count
    return size

def visit(everything):
    queue = []
    node = everything[0]
    edges = everything[1]
    colour = everything[2]
    pred = everything[3]
    steps = everything[4]

    size = 0
    colour[node] = "G"
    queue.append(node)
    while len(queue) != 0:
        u = queue[0]
        for out in range(len(edges[u])):
            nextnode = int(edges[u][out])
            if colour[nextnode] == "W":
                colour[nextnode] = "G"
                pred[nextnode] = u
                size += 1
                steps[nextnode] = steps[u]+1
                queue.append(nextnode)
            elif colour[nextnode] == "G":
                size += 1
        
        queue = queue[1:]
        colour[u] = "B"
    return size


info = []

for line in sys.stdin:
    info.append(line.strip())

sizes = seperate(info)
for i in range(len(sizes)):
    print("Graph {} has size {}.".format(i+1, sizes[i]))
