from collections import deque
q = deque()
n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

def bfs(start):
    chk = [False] * (n + 1)
    q.append(start)
    chk[start[0]] = True
    total = 0
    while q:
        node, t = q.popleft()
        for n_node, cur_t in graph[node]:
            if not chk[n_node]:
                chk[n_node] = True
                q.append([n_node, cur_t + t])
                total += (cur_t + t)
    return total

for i in range(1, n + 1):
    print(bfs([i, 0]))
