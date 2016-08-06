import sys
mod = 10**9 + 7

def sgn(v):
    return (v > 0) - (v < 0)

def compute_answer():
    v.sort(key=abs, reverse=True)
    prod = 1
    sg = 1
    print('k')
    print(k)
    print('v')
    print(v)
    for a in range(k):
        prod *= v[a]
        prod %= mod
        print('v[a]')
        print(v[a])
        print('sgn value ->')
        print(sgn(v[a]))
        sg *= sgn(v[a])

    if sg >= 0:
        return prod

    if max(v) <= 0:
        prod = 1
        for a in range(-k,0):
            prod *= v[a]
            prod %= mod
        return prod

    i, j = find_pair(lambda w: w >= 0)
    I, J = find_pair(lambda w: w <= 0)
    if I >= 0 and v[j] * v[I] < v[i] * v[J]:
        i = I
        j = J

    prod = v[j]
    for a in range(k):
        if a != i:
            prod *= v[a]
            prod %= mod
    return prod

def find_pair(comp):
    i = k-1
    while i >= 0 and comp(v[i]): i -= 1
    j = k
    while j < n and not comp(v[j]): j += 1
    if j == n: j = i
    return i, j

T = int(sys.stdin.readline())

for cas in range(T):
    n, k = map(int, sys.stdin.readline().split())
    v = list(map(int, sys.stdin.readline().split()))

    #print(n)
    #print(k)
    #print(v)

    ans = compute_answer()
    print(ans)
