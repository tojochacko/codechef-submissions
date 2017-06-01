import sys

T = int(sys.stdin.readline())
while T:
    T -=1
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    for i in range(0, N-1):
        if i%2 == 0:
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
        elif i%2 != 0:
            if A[i] < A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]

    print(' '.join(str(a) for a in A))
