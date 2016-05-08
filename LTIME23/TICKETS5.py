T = int(input())

while(T > 0):
    S = input() 
    answerArr = {}
    for c in S:
        if c not in answerArr:
            answerArr[c] = 0
        else:
            answerArr[c] += 1 
        
    if len(answerArr) == 2:
        print('YES')
    else:
        print('NO')
    T -= 1

