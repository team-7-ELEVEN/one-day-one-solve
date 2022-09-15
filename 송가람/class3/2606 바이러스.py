from collections import deque
q = deque()
n = int(input())
m = int(input())

link = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

def bfs(start):
    q.append(start)
    chk[start] = True
    while q:
        node = q.popleft()
        for i in link[node]:
            if not chk[i]:
                q.append(i)
                chk[i] = True
    return chk.count(True) - 1

chk = [False] * (n + 1)

print(bfs(1))