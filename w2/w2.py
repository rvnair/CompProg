import Queue
import sys

arr = raw_input().split()
dest = int(arr[0])
numEdge = int(arr[1])
graph = {}


#Build Graph
for i in range(numEdge):
    arr = raw_input().split()
    v1 = int(arr[0])
    v2 = int(arr[1])
    dist = int(arr[2])
    if v1 in graph.keys():
        adjMap = graph.get(v1)
        if v2 in adjMap.keys() :
            if dist < adjMap.get(v2):
                adjMap[v2] = dist
        else:
            adjMap[v2] = dist
    else:
        graph[v1] = {v2: dist}

    if v2 in graph.keys():
        adjMap = graph.get(v2)
        if v1 in adjMap.keys() :
            if dist < adjMap.get(v1):
                adjMap[v1] = dist
        else:
            adjMap[v1] = dist
    else:
        graph[v2] = {v1:dist}

#Run Dijkstras on Graph
class Path():
    def __init__(self):
        self.cost = 0;
        self.prev = sys.maxint

unvisited = graph.keys()

cost = []
for i in range(dest):
    x = Path()
    x.cost = sys.maxint
    cost.append(x)
q = Queue.Queue()
q.put(1)
cost[0].cost = 0
cost[0].prev = 0
unvisited.remove(1)
while not(q.empty()):
    curr = q.get()
    currCost = cost[curr - 1].cost

    for neighbor in graph.get(curr).keys():
        if currCost + graph.get(curr).get(neighbor) < cost[neighbor - 1].cost :
            cost[neighbor - 1].cost = currCost + graph.get(curr).get(neighbor)
            cost[neighbor - 1].prev = curr

        if neighbor in unvisited:
            q.put(neighbor)
            unvisited.remove(neighbor)



if cost[dest - 1].cost == sys.maxint:
    print -1
else:
    path = [dest]
    x = cost[dest - 1].prev
    while not (x == 0):
        path.append(x)
        x = cost[x - 1].prev
    for i in reversed(path):
        print i,