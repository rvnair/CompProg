
a = []
b = []
loop  = input()

def dfs(src, dest):
    if (a[dest][0] < a[src][0] and a[src][0] < a[dest][1]) or (a[dest][0] < a[src][1] and a[src][1] < a[dest][1]):
        return "YES"
    b[src] = 1
    for i in range(len(a)):
        if b[i] == 0:
            if (a[i][0] < a[src][0] and a[src][0] < a[i][1]) or (a[i][0] < a[src][1] and a[src][1] < a[i][1]):
                if(dfs(i, dest) == "YES"):
                    return "YES"
    return "NO"

for gav in range(loop):
    line = [int(x) for x in raw_input().split(" ")]
    if line[0] == 1:
        a.append(line[1:])
    else:
        b = [0 for i in a]
        print dfs(line[1]-1,line[2]-1)