import sys

# no of test cases
tests = int(input())

if tests > 100 or tests < 1:
    sys.exit()

while tests != 0:
    tests -= 1
    # no of activities and origin
    activityMeta = input()
    activityMetaList = activityMeta.split(' ')
    noofActivities = int(activityMetaList[0])
    originofUser = activityMetaList[1]

    laddus = 0
    while noofActivities != 0:
        noofActivities -= 1
        activityType = input()
        activityTypeList = activityType.split(' ')

        if activityTypeList[0] == 'CONTEST_WON':
            rank = int(activityTypeList[1])
            laddus += 300 + (20 - rank)
        elif activityTypeList[0] == 'TOP_CONTRIBUTOR':
            laddus += 300
        elif activityTypeList[0] == 'BUG_FOUND':
            severity = int(activityTypeList[1])
            laddus += severity
        elif activityTypeList[0] == 'CONTEST_HOSTED':
            laddus += 50

    if originofUser == 'INDIAN':
        ans = int(laddus / 200)
    elif originofUser == 'NON_INDIAN':
        ans = int(laddus / 400)

    print(ans)