import sys

newList = list(map(int, sys.stdin.readline().split(' ')))
n = newList[0]
k = newList[1]
ans = 0

while n:
    n -= 1
    x = int(sys.stdin.readline()) 
    if x%k == 0:
        ans += 1
print(ans)
