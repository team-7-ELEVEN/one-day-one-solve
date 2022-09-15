from collections import deque

n = int(input())

graph = [list(map(int, input())) for _ in range(n)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

cnt_list = []

def bfs(i, j):
    cnt = 1
    q = deque()
    q.append((i, j))
    graph[i][j] = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if graph[ny][nx] == 1:
                    q.append((ny, nx))
                    graph[ny][nx] = 0
                    cnt += 1
                    
    cnt_list.append(cnt)
    return(cnt_list)
    
num = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i, j)
            num += 1

print(num)
cnt_list.sort()
for i in cnt_list:
    print(i)
