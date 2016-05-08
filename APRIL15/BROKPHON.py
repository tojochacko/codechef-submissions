t = int(input())

#@TODO: just have to consider the edge case
while(t!=0):
    n = input() # n is not necessary for me
    numbers = list(map(int, input().split()))
    prev = numbers[0];
    answer = 0
    for i in numbers:
        if i != prev:
            answer += 2
        prev = i
    t -= 1
    print(answer)

