from collections import deque
N, M = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
graph = [list(map(int, input())) for _ in range(N)]


def bfs(n, m):
    q = deque()
    q.append([n, m])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append([nx, ny])
                    
    return graph[N-1][M-1]

print(bfs(0, 0))


    
