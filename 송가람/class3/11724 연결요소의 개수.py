import sys
from collections import deque
input = sys.stdin.readline
q = deque()
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

def bfs(start):
    q.append(start)
    chk[start] = True
    while q:
        node = q.popleft()
        for i in graph[node]:
            if not chk[i]:
                chk[i] = True
                q.append(i)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

chk = [False] * (N + 1)
cnt = 0


for i in range(1, N + 1):
    if not chk[i]:  
        if not graph[i]:  
            cnt += 1  
            chk[i] = True 
        else: 
            bfs(i)  
            cnt += 1 
print(cnt)



