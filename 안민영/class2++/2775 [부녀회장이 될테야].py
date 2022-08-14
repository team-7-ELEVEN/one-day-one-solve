from sys import stdin
input = stdin.readline 

a = [[0 for _ in range(15)] for _ in range(15)]

# 1호마다
for i in range(1, 15) :
    a[i][1] = 1

# 0층에는
for i in range(1, 15) :
    a[0][i] = a[0][i-1] + 1

for i in range(1, 15) :
    for j in range(1, 15) :
        a[i][j] = a[i][j-1] + a[i-1][j]

t = int(input())
for _ in range(t) :
    k = int(input()) # 층
    n = int(input()) # 호
    print(a[k][n])
