import sys
from collections import deque
dq = deque()
input = sys.stdin.readline

for _ in range(int(input())):
    command = input().strip()

    if command == "pop":
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif command == "size":
        print(len(dq))
    elif command == "empty":
        if dq:
            print(0)
        else:
            print(1)
    elif command == "front":
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif command == "back":
        if dq:
            print(dq[-1])
        else:
            print(-1)
    else:
        dq.append(int(command.split()[-1]))
