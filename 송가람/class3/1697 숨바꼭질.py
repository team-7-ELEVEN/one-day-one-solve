from collections import deque
N, K = map(int, input().split())

distance = [0] * 100001

def bfs(n):
    q = deque()
    q.append(n)
    while q:
        i = q.popleft()
        if i == K:
            return(distance[i])
        for ni in (i - 1, i + 1, i * 2):
            if ni >= 0 and ni <= 100000 and not distance[ni]:
                distance[ni] = distance[i] + 1
                q.append(ni)

print(bfs(N))

