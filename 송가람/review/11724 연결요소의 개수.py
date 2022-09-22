import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

chk = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    q = deque()
    q.append(start)
    chk[start] = True
    while q:
        n = q.popleft()
        for i in graph[n]:
            if not chk[i]:
                q.append(i)
                chk[i] = True

cnt = 0
for i in range(1, N + 1):
    if not chk[i]:
        if not graph[i]:
            cnt += 1
            continue
        else:
            bfs(i)
            cnt += 1

print(cnt)

