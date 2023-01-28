from collections import deque
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
q = deque()

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (1 + N)

def bfs(start):
    q.append(start)
    visited[start] = True
    while q:
        node = q.popleft()
        for n in graph[node]:
            if not visited[n]:
                visited[n] = True
                q.append(n)


cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        if not graph[i]:
            cnt += 1
        else:
            bfs(i)
            cnt += 1
print(cnt)