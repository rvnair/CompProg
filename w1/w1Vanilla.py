import Queue

#Read in inputs
numGraphs = int(raw_input())

for i in range(numGraphs):
    arr = raw_input().split()
    numVertex = int(arr[0])
    numEdge = int(arr[1])
    startNode = int(arr[2])
    maxDist = int(arr[3])

    #Build adjacency list
    graph = {}
    for x in range(numEdge):
        arr = raw_input().split()
        v1 = int(arr[0])
        v2 = int(arr[1])
        if(v1 in graph):
            temp = graph[v1]
            if not (v2 in temp):
                temp.append(v2)
            graph[v1] = temp
        else:
            graph[v1] = [v2]
        if (v2 in graph):
            temp = graph[v2]
            if not (v1 in temp):
                temp.append(v1)
            graph[v2] = temp
        else:
            graph[v2] = [v1]

    #BFS to find connected components
    q = Queue.Queue()
    toDo = graph.keys()
    count = numVertex - len(graph.keys()) #Count single nodes
    inRange = []
    findRange = False
    while not (len(toDo) == 0):


        if(startNode in toDo):
            q.put(startNode)
            visited = [startNode]
            toDo.remove(startNode)
            inRange.append(startNode)
            findRange = True
        else:
            q.put(toDo[0])
            visited = [toDo[0]]
            toDo.remove(toDo[0])
            findRange = False

        while not (q.empty()):
            node = q.get()
            for neighbor in graph[node]:
                if not (neighbor in visited):
                    q.put(neighbor)
                    visited.append(neighbor)

                    #Take off the list
                    if(neighbor in toDo):
                        toDo.remove(neighbor)

                    if(findRange and maxDist > 0):
                        inRange.append(neighbor)
        maxDist = maxDist - 1
        count = count + 1
    if(len(inRange) == 0):
        inRange.append("SINGLE NODE")
    print count, len(inRange)