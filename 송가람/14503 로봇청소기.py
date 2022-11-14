from collections import deque
N, M = map(int, input().split())
r, c, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 상 0 / 우 1 / 하 2 / 좌 3
# 3 => l: 0
# 1 => l: 2
# 2 => l: 1 
# 0 => l: 3
def n_direction(curr):
    if curr == 3:
        return 0
    elif curr == 2:
        return 1 
    elif curr == 1:
        return 2 
    elif curr == 0:
        return 3 

def bfs(r, c, d):
    q = deque()
    q.append([r, c, d])
    while q:
        y, x, curr_d = q.popleft()
        nd = n_direction(curr_d)
        ny = y + dy[nd]
        nx = x + dx[nd]
        if 0 <= ny < N and 0 <= nx < M:
            if graph[ny][nx] == 0:
                graph[ny][nx] = -1
                q.append([ny, nx, nd])
