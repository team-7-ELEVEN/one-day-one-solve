from collections import deque
import math
q = deque()
n, l = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(l):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

def bfs(s):
    q.append([s, 0])
    chk = [s]
    kevin = 0
    while q:
        f = q.popleft()
        kevin += f[1]
        for i in range(n + 1):
            if graph[f[0]][i] == 1 and (i not in chk):
                q.append([i, f[1] + 1 ])
                chk.append(i)
    
    return kevin

min = math.inf

for i in range(1, n + 1):
    kevin = bfs(i)
    if kevin < min:
        min = kevin
        min_p = i
print(min_p)
        

        
