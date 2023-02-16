from collections import deque
N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
chk = [[False] * M for _ in range(N)]
dx = [0, 0, 1]
dy = [-1, 1, 0]

def dp(X, Y):
    q = deque()
    q.append([X, Y])
    chk[X][Y] = True
    while q:
        x, y = q.popleft()
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not chk[nx][ny]:
                    if board[nx][ny] < board[x][y] + board[nx][ny]:
                        board[nx][ny] += board[x][y]
                        q.append([nx, ny])
                        chk[nx][ny] = True
                    else:
                        chk[nx][ny] = True

    return board[N - 1][M - 1]

print(dp(0, 0))



