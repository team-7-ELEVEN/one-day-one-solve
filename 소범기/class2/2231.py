import sys
input = sys.stdin.readline

N=int(input())
i = 1
while True:
    sum_ = 0
    temp = sum(list(map(int,str(i))))
    temp += i
    if temp == N:
        print(i)
        break
    elif i >= N:
        print(0)
        break
    i+=1