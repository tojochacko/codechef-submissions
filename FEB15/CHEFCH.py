def prepareMap():
    for i in range(100000):
        if(i % 2 == 0):
            map1.append('+')
            map2.append('-')
        else:
            map1.append('-')
            map2.append('+')

def getCount(s, l):
    count = 0
    i = 0
    for eachChar in s:
        if(eachChar != l[i]):
            count += 1
        i += 1
    return count

t = int(input())
map1 = []
map2 = []
prepareMap()

while(t!=0):
    #for each test case
    s = input()
    count1 = getCount(s, map1)
    count2 = getCount(s, map2)
    t -= 1
    if(count1 < count2):
        print(count1)
    else:
        print(count2)

