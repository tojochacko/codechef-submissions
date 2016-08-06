import sys

newlist = list(map(int, sys.stdin.readline().split()))
newlist.sort()

if newlist[0]/newlist[1] == newlist[2]/newlist[3]:
    print('Possible')
else:
    print('Impossible')

