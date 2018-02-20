import sys
def calcTime(p, rc, rt):
    return long(p * (p - 1) / 2 + p / rc * rt)

def binSearch(n, rc, rt, time):
    low = 0
    high = sys.maxint
    mid = -1
    while low + 1 < high:
        mid = (low + high) / 2
        if calcTime(mid, rc, rt) < time:
            low = mid
        else:
            high = mid
    return mid

loops = long(raw_input())
for i in range(loops):
    arr = raw_input().split()
    totalTime = long(arr[0])
    roomCap = long(arr[1])
    roomTime = long(arr[2])
    print binSearch(10000000, roomCap, roomTime, totalTime)
