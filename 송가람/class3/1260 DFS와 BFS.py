from collections import deque
q = deque()
N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

def bfs(V):
    q.append(V)
    chk = [V]
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(N + 1):
            if graph[v][i] == 1 and (i not in chk):
                q.append(i)
                chk.append(i)


def dfs(v, chk = []):
    chk.append(v)
    print(v, end=' ')
    for i in range(N + 1):
        if graph[v][i] == 1 and (i not in chk):
            dfs(i, chk)

dfs(V)
print()
bfs(V)

