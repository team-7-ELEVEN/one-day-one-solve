import sys
input = sys.stdin.readline
N = int(input())
data = []
for _ in range(N):
    t = int(input())
    data.append(t)

data.sort()
for i in data:
    print(i)