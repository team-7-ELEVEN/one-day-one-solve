from collections import deque
from sys import stdin
input = stdin.readline

def empty(queue) :
    if len(queue) < 1 :
        return 1
    else : return 0 

queue = deque()
n = int(input())

for _ in range(n) :
    ins = input().split()

    if ins[0] == 'push' :
        queue.append(ins[1])
    elif ins[0] == 'pop' :
        if (empty(queue)) : print(-1)
        else : print(queue.popleft())
    elif ins[0] == 'front' :
        if (empty(queue)) : print(-1)
        else : print(queue[0])
    elif ins[0] == 'back' :
        if (empty(queue)) : print(-1)
        else : print(queue[-1])
    elif ins[0] == 'size' :
        print(len(queue))
    elif ins[0] == 'empty' :
        print(empty(queue))
