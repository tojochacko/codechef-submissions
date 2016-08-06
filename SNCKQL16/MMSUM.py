import sys

def maximalSum(numList):
    maxOf = maxHere = numList[0]
    for num in numList[1:]:
        maxHere = max(num, maxHere + num)
        maxOf = max(maxOf, maxHere)
    return maxOf

T = int(sys.stdin.readline())

for case in range(T):
    N = int(sys.stdin.readline()) #not really required here
    listOfNums = list(map(int, sys.stdin.readline().split(' ')))
    maxS = maximalSum(listOfNums)

    for i, v in enumerate(listOfNums):
        #newList = listOfNums.copy()
        #newList.pop(i)
        #maxS = max(maxS, maximalSum(newList))

    print(ans)

     
