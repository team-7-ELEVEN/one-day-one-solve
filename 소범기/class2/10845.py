from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
dq = deque([])
for _ in range(N):
    order = list(input().split())
    if order[0] == "push":
        dq.append(int(order[1]))
    elif order[0] == "pop":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif order[0] == "size":
        print(len(dq))
    elif order[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif order[0] == "back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
