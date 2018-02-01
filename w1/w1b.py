arr = raw_input().split()
len = int(arr[0])
hop = int(arr[1])
tpos = -1;
gpos = -1;
count = 1;
field = raw_input()

for c in field:
    if c == 'G':
        gpos = count
    if c == 'T':
        tpos = count
    count = count + 1

if not(gpos % hop == tpos % hop):
    print "NO"
if (gpos > tpos):
    while not (gpos == tpos):
        if (field[gpos - 1] == '#'):
            print "NO"
            break;
        gpos = gpos - hop
    if (gpos == tpos):
        print "YES"
else:
    while not(gpos == tpos):
        if(field[gpos -1] == '#'):
            print "NO"
            break;
        gpos = gpos + hop
    if(gpos == tpos):
        print "YES"
