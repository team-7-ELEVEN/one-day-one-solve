from collections import deque
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(Y, X):
    global graph
    q = deque()
    q.append([Y, X])
    update[Y][X] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and not update[ny][nx]:
                if graph[ny][nx] == 0:
                    graph[y][x] -= 1
                    if graph[y][x] < 0:
                        graph[y][x] = 0
                else:
                    q.append([ny, nx])
                    update[ny][nx] = True

year = 0
while True:
    # cnt를 초기화해야함 => 아니면 매년 마다 cnt값이 갱신됨
    cnt = 0
    year += 1
    update = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and not update[i][j]:
                cnt += 1
                bfs(i, j)
    
    if cnt == 0:
        print(0)
        break
    elif cnt >= 2:
        # year에서 -1 해줘야함
        print(year - 1)
        break

        
