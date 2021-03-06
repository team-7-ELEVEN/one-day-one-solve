# 스택
# 실버 4

import sys

N = int(input())
stack = []

for _ in range(N):
    x = sys.stdin.readline().split()
    if x[0] == "push":
        stack.append(x[1])
    elif x[0] == "pop":
        if stack:
            print(stack.pop(-1))
        else:
            print(-1)
    elif x[0] == "size":
        print(len(stack))
    elif x[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif x[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
