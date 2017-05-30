import sys
S = int(sys.stdin.readline())
for j in range(0, S):
    N = int(sys.stdin.readline())
    H = list(map(int, input().split()))
    flag = 0
    if N % 2 == 0:
        print('no')
        continue
    elif H[0] != 1:
        print('no')
        continue
    else:
        for i in range(0, N//2 + 1):
            if i > 0:
                if H[i]-H[i-1] == 1:
                    continue
                else:
                    print('no')
                    flag = 1
                    break
            elif i == 0:
                continue

        if flag == 0:
            for i in range(N//2 + 1, N):
                if H[i-1]-H[i] == 1:
                    continue
                else:
                    print('no')
                    flag = 1
                    break

        if flag == 0:
            print('yes')
