import Queue
import sys

graphNum = int(raw_input())

for x in range(graphNum):
    arr = raw_input().split()
    dest = int(arr[0])
    numEdge = int(arr[1])
    graph = {}

    #Build Graph
    for i in range(numEdge):
        arr = raw_input().split()
        v1 = int(arr[0])
        v2 = int(arr[1])
        mph = float(arr[2])
        miles = float(arr[3])
        dist = int(round(miles / mph, 0))
        if v1 in graph.keys():
            adjMap = graph.get(v1)
            if v2 in adjMap.keys() :
                if dist < adjMap.get(v2):
                    adjMap[v2] = dist
            else:
                adjMap[v2] = dist
        else:
            graph[v1] = {v2:dist}

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
    # Set up
    unvisited = graph.keys()
    cost = []
    for i in range(dest):
        cost.append(sys.maxint)
    q = Queue.Queue()
    q.put(1)
    cost[0] = 0
    unvisited.remove(1)
    #Actual Dijkstra
    while not(q.empty()):
        curr = q.get()
        currCost = cost[curr - 1]
        for neighbor in graph.get(curr).keys():
            # Store lowest cost, add to queue if not visited
            if currCost + graph.get(curr).get(neighbor) < cost[neighbor - 1] :
                cost[neighbor - 1] = currCost + graph.get(curr).get(neighbor)
                if (neighbor in unvisited):
                    q.put(neighbor)
                    unvisited.remove(neighbor)

    print cost[dest - 1]