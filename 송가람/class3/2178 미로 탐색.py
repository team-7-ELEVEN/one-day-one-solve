from collections import deque
N, M = map(int, input().split())

dy = [1, -1, 0, 0]
dx = [0, 0, -1 ,1]
graph = [list(map(int, input())) for _ in range(N)]

def bfs(n, m):
    q = deque()
    q.append([n, m])
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny >= 0 and ny < N and nx >= 0 and nx < M:
                if graph[ny][nx] == 1:
                    q.append([ny, nx])
                    graph[ny][nx] = graph[y][x] + 1

    return graph[n - 1][m - 1]

print(bfs(0, 0))