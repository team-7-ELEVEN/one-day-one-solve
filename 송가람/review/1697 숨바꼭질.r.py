from collections import deque
N, K = map(int, input().split())

distance = {}
def bfs(ipt):
    q = deque()
    q.append(ipt)
    distance[ipt] = 0
    while q:
        n = q.popleft()
        if n == K:
            return distance[n]
        for i in [n - 1, n + 1, n * 2]:
            if 0 <= i <= 100000 and not i in distance:
                distance[i] = distance[n] + 1
                q.append(i)

print(bfs(N))
