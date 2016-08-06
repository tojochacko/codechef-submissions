import sys

T = int(input())

while T:
    T -= 1 
    N = int(input())
    ans = 0
    prevTimeTable = 0

    timeTable = input()
    timeTableList = timeTable.split(' ') 
    timeRequired = input()
    timeRequiredList = timeRequired.split(' ')

    for i in range(0, len(timeTableList)):
        moment = int(timeTableList[i]) - int(prevTimeTable)
        if moment >= int(timeRequiredList[i]):
            ans += 1
        prevTimeTable = timeTableList[i]

    print(ans)
