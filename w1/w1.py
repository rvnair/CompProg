import Queue
import math

arr = raw_input().split()
start = int(arr[0])
goal = int(arr[1])

if(goal <= start):
    print start - goal
else:
    q = Queue.Queue()
    currStep = 1
    visit = []
    q.put(start)
    prevSize = 1
    currSize = 1
    while not (goal in visit):
        curr = q.get()
        if 2 * curr not in visit:
            q.put(2 * curr)
            visit.append(2 * curr)
        if curr - 1 not in visit:
            q.put(curr - 1)
            visit.append(curr - 1)
        if(prevSize * 2 == currSize):
            currStep = currStep + 1
            prevSize = currSize
        currSize = currSize + 1
    print currStep