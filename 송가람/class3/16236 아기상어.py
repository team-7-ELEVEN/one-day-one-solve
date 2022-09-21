from collections import deque
N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

dy = [1, 0, 0, -1]
dx = [0, -1, 1, 0]

chk = [[False] * N for _ in range(N)]

def bfs(i, j):
    size = 2
    eat = 0
    cnt = 0
    q = deque()
    q.append([i, j])
    graph[i][j] = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and graph[ny][nx] <= size and not chk[ny][nx]:
                cnt += 1
                chk[ny][nx] = True
                q.append([ny, nx])
                if 0 < graph[ny][nx] < size:
                    chk = [[False] * N for _ in range(N)]
                    chk[ny][nx] = True
                    eat += 1
                    if eat == size:
                        size += 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            bfs(i, j)

print(chk)                   
