from sys import stdin
from collections import deque
input = stdin.readline()
n = int(input())

def distance(a, b):
    ay, ax = a
    by, bx = b
    return abs(ay - by) + abs(ax - bx)

def bfs(initial, flag):
    q.append(initial)
    visited.append(initial)
    while q:
        now = q.popleft()
        for i in store:
            dis = distance(i, now)
            if dis <= 1000 and not (i in visited):
                if distance(i, festival) <= 1000:
                    flag = True
                    return flag
                q.append(i)
                visited.append(i)

for _ in range(n):
    n_store = int(input())
    home = list(map(int, input().split()))
    store = [list(map(int, input().split())) for _ in range(n_store)]
    festival = list(map(int, input().split()))
 
    q = deque()
    visited = []
    flag = False
    d = distance(festival, home)
    if d <= 1000:
        print("happy")
    elif store:
        flag = bfs(home, flag)
        if flag:
            print("happy")
        else:
            print("sad")
    else:
        print("sad")

