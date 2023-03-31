from collections import deque
f = [list(input()) for _ in range(12)]
n = 6
m = 12
dic = {}

# 필드 가로로 눕히기
field = [[] for _ in range(6)]
for i in range(6):
    for j in range(11, -1, -1):
        field[i].append(f[j][i])

def bfs(X, Y, c):
    q = deque()
    q.append([X, Y])
    visited = [[False] * 12 for _ in range(6)]
    pang = []
    is_pang = 0
    dx = [0,0,1,-1]
    dy = [1, -1, 0, 0]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < 6 and 0 <= ny < 12 and not visited[nx][ny]:
                visited[nx][ny] = True
                if field[nx][ny] == c:
                    pang.append([nx, ny])
                    q.append([nx, ny])

    if len(pang) >= 4:
        is_pang = 1
        for x1, y1 in pang:
            field[x1][y1] = '.'

    return is_pang

def gravity():
    for i in range(6):
        c = []
        for j in range(12):
            if field[i][j] != '.':
                c.append(field[i][j])
        field[i] = c + (['.'] * (12 - len(c)))

ans = 0
while True:
    pang = 0
    for l in range(6):
        for k in range(12):
            if field[l][k] != '.':
                pang += bfs(l, k, field[l][k])
    
    if pang:
        ans += 1
    else:
        print(ans)
        break
    gravity()
    

