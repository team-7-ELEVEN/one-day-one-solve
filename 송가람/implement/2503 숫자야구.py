import itertools
n = int(input())
arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num = list(itertools.permutations(arr, 3))

for _ in range(n):
    n, s, b = map(int, input().split())
    n = list(str(n))
    rm = 0
    for i in range(len(num)):
        strike = ball = 0
        i -= rm
        for j in range(3):
            if num[i][j] == n[j]:
                strike += 1
            elif n[j] in num[i]:
                ball += 1

        if strike != s or ball != b:
            num.remove(num[i])
            rm += 1

print(len(num))
        
