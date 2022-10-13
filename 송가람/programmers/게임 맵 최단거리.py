from collections import deque


def solution(maps):
    answer = 0
    q = deque()
    n = len(maps)
    m = len(maps[0])
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    def bfs(Y, X):
        q.append([Y, X])
        while q:
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0<= ny < n and 0<= nx < m and maps[ny][nx] == 1:
                    maps[ny][nx] = maps[y][x] + 1
                    q.append([ny, nx])
        return maps[n - 1][m - 1]

    ans = bfs(0, 0)
    if ans == 1:
        return -1
    else: 
        return ans



maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))