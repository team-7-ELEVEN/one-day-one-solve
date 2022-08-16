import sys
input = sys.stdin.readline
N = int(input())
data = []
for i in range(N):
    age,name = input().split()
    data.append((i,int(age),name)) 

sol_set = sorted(data,key = lambda x : (x[1],x[0]))
for i in sol_set:
    print(i[1],i[2])