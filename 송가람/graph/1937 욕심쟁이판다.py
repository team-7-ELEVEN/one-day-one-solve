import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dp = [[-1] * n for _ in range(n)]

def dfs(x, y):

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[x][y] < board[nx][ny]:
                result = dfs(nx, ny) + 1
                dp[x][y] = max(result, dp[x][y])

    return dp[x][y]

max_r = 0
for i in range(n):
    for j in range(n):
        r = dfs(i, j)
        if max_r < r:
            max_r = r
print(max_r)
