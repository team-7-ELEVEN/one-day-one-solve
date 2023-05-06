import math
n = int(input())
k = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

mid = math.ceil(n / 2)
board = [[0] * n for _ in range(n)]
x, y = mid - 1, mid - 1
board[x][y] = 1
ans = ''

idx = 0
for i in range(1, n):
    if i == (n - 1):
        for _ in range(3):
            for _ in range(i):
                if idx == 4:
                    idx = 0
                nx = x + dx[idx]
                ny = y + dy[idx]
                board[nx][ny] = board[x][y] + 1
                if board[nx][ny] == k:
                    ans = f'{nx + 1} {ny + 1}'
                x, y = nx, ny
            idx += 1
    else:
        for _ in range(2):
            for _ in range(i):
                if idx == 4:
                    idx = 0
                nx = x + dx[idx]
                ny = y + dy[idx]
                board[nx][ny] = board[x][y] + 1
                if board[nx][ny] == k:
                    ans = f'{nx + 1} {ny + 1}'
                x, y = nx, ny
            idx += 1

for row in board:
    print(*row)
if k == 1:
    print(mid, mid)
else:
    print(ans)