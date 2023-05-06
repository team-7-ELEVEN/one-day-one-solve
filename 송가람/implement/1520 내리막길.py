# M, N = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(M)]
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# # 상 하 좌 우
# visited = [[False] * N for _ in range(M)]

# def dfs(y, x):
#     visited[y][x] = True
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if 0 <= ny < M and 0 <= nx < N:
#             if not visited[ny][nx]:
#                 print(board[ny][nx], board[y][x])
#                 if board[ny][nx] < board[y][x]:
#                     visited[ny][nx] = True
#                     dfs(ny, nx)
#                 else:
                    
# print(visited)
# dfs(0, 0)

import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

def dfs(sx, sy):
    # 도착 지점에 도달하면 1(한 가지 경우의 수)를 리턴
    if sx == m-1 and sy == n-1:
        return 1

    # 이미 방문한 적이 있다면 그 위치에서 출발하는 경우의 수를 리턴
    if dp[sx][sy] != -1:
        return dp[sx][sy]
    
    dp[sx][sy] = 0
    for i in range(4):
        nx, ny = sx + dx[i], sy + dy[i]
 
        if 0 <= nx < m and 0 <= ny < n:
            print(graph[sx][sy], graph[nx][ny])
            if graph[sx][sy] > graph[nx][ny]:
                dp[sx][sy] += dfs(nx, ny)
    
    return dp[sx][sy]


m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
dx, dy = [1,-1,0,0], [0,0,1,-1]
# 하 상 우 좌
print(dfs(0,0)) 






