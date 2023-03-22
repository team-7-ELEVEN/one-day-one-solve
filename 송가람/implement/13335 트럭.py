from collections import deque
n, w, l = map(int, input().split())
dq = deque([0] * (w - 1))
trucks = deque(list(map(int, input().split())))
cnt = 1
while trucks:
    if sum(dq) + trucks[0] <= l and len(dq) + 1 <= w:
        dq.append(trucks.popleft())
    else:
        dq.append(0)
    cnt += 1
    dq.popleft()

while dq:
    dq.popleft()
    cnt += 1

print(cnt)