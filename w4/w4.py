numShops = int(raw_input())
shops = []
for x in raw_input().split():
    shops.append(int(x))
shops.sort()
numQueries = int(raw_input())
for x in range(numQueries):
    money = int(raw_input())
    index = len(shops) / 2
    found = True
    low = 0
    high = len(shops) - 1
    mid = -1
    if(money >= shops[high]):
        print high + 1
    else:
        while low + 1 < high:
            mid = (low + high) / 2
            if shops[mid] <= money:
                low = mid
            else:
                high = mid
        mid = (low + high) / 2
        if(money < shops[mid]):
            print 0
        else:
            print mid + 1