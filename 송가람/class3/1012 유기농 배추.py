# 덱으로 푸는법
from collections import deque
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0] 

def bfs(y, x):
    q = deque()
    q.append([y, x])
    field[y][x] = 0
    while q: 
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if field[ny][nx] == 1:
                    field[ny][nx] = 0
                    q.append([ny, nx])
                    
for _ in range(int(input())):
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1

    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)

# 재귀로 풀었을 때
# import sys
# sys.setrecursionlimit(10000)

# def dfs(y, x):
#     dy = (0, 1, 0, -1)
#     dx = (1, 0, -1, 0)
#     for k in range(4):
#         ny = y + dy[k]
#         nx = x + dx[k]
#         if 0 <= ny < h and 0 <= nx < w:
#             if field[ny][nx] == 1:
#                 field[ny][nx] = -1
#                 dfs(ny, nx)

# for _ in range(int(input())):
#     w, h, b = map(int, input().split())
#     field = [[0] * w for _ in range(h)]
#     cnt = 0

#     for _ in range(b):
#         m, n = map(int, input().split())
#         field[n][m] = 1
        
#     for i in range(h):
#         for j in range(w):
#             if field[i][j] > 0:
#                 dfs(i, j)
#                 cnt += 1

#     print(cnt)

