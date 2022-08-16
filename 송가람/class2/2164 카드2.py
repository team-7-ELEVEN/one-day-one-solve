import sys
from collections import deque
dq = deque()
input = sys.stdin.readline

N = int(input())
for i in range(1, N+1):
    dq.append(i)

while True:
    if len(dq) == 1:
        print(dq[0])
        break
    dq.popleft()
    left = dq.popleft()
    dq.append(left)

    
