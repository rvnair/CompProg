import sys
gameCount = int(raw_input())
for x in range(gameCount):
    arr = raw_input().split()
    goalRoom = int(arr[0])
    edgeNum = int(arr[1])
    startHealth = -int(arr[2])
    graphList = {}
    for e in range(edgeNum):
        list = raw_input().split()
        src = int(list[0])
        dest = int(list[1])
        w = -int(list[2])
        if src in graphList.keys():
            if dest in graphList[src].keys():
                if graphList[src][dest] > w:
                    graphList[src][dest] = w
            else:
                graphList[src][dest] = w
        else:
            graphList[src] = {dest : w}
    dist = [startHealth]
    for d in range(goalRoom - 1):
        dist.append(sys.maxint)
    for j in range(goalRoom - 1):
        for v in graphList.keys():
            for u in graphList[v].keys():
                if dist[u-1] > dist[v - 1] + graphList[v][u]:
                    dist[u-1] = dist[v - 1] + graphList[v][u]
    if dist[goalRoom - 1] == sys.maxint:
        print -1
    elif dist[0] < startHealth:
        print "infinity"
    else:
        print dist[goalRoom - 1] * -1