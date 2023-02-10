from collections import deque

n = int(input())
q = deque(list(range(1, n + 1)))
ans = []
while q:
    if q:
        ans.append(q.popleft())
        if q:
            q.append(q.popleft())

print(*ans)