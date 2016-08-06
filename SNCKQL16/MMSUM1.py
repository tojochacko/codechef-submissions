for cas in range(int(input())):
    n = int(input())
    a = list(map(int, input().strip().split()))
    pref = [0]*n
    suff = [0]*n
    curr = 0
    for i in range(n):
        pref[i] = curr = max(curr, 0) + a[i]
    curr = 0
    for i in range(n-1,-1,-1):
        suff[i] = curr = max(curr, 0) + a[i]

    print(pref + suff)
    print (max(pref + suff + [pref[i-1] + suff[i+1] for i in range(1,n-1)]))
