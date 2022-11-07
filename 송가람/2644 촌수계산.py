from collections import deque
q = deque()
n = int(input())
a, b = map(int, input().split())

family = [[] for _ in range(n + 1)]

for i in range(int(input())):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

print(family)

chk = [False] * (n + 1)
ans = []

def bfs(start):
    chk[start] = True
    cnt = 0
    q.append([start, cnt])
    while q:
        node, cnt = q.popleft()
        for i in family[node]:
            if not chk[i]:
                if i == b:
                    return cnt + 1
                chk[i] = True
                q.append([i, cnt + 1])
            
                
    return -1

print(bfs(a))
