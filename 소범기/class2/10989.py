import sys
input =sys.stdin.readline
list_= [0] * 10001
N = int(input())
for _ in range(N):
    x= int(input())
    list_[x] +=1

for i in range(len(list_)):
    if list_[i] == 0:
        continue
    else:
        for _ in range(list_[i]):
            print(i)