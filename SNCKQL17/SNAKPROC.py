import sys

R = int(sys.stdin.readline())
while R:
    R -= 1
    L = int(sys.stdin.readline())
    report = sys.stdin.readline().rstrip('\n')
    lenreport = len(report)

    answer = 'Valid'
    bracketOpen = False

    if lenreport == L:
        for i in range(0, lenreport):
            currentC = report[i]

            if currentC == 'H':
                if bracketOpen == True:
                    break;
                bracketOpen = True
            elif currentC == 'T' and bracketOpen == True:
                bracketOpen = False
            elif currentC == 'T' and bracketOpen == False:
                bracketOpen = True
                break;

        if bracketOpen == True:
            answer = 'Invalid'

        print(answer)
    else:
        pass


