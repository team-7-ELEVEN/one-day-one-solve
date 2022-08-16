import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    M = int(input())
    if M == 0:
        stack.pop()
    else:
        stack.append(M)
#print(stack)
print(sum(stack))