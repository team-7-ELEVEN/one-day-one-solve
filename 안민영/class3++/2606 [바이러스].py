from collections import deque
from sys import stdin
input = stdin.readline

node = int(input())
edge = int(input())
graph = [[0 for _ in range(node+1)] for _ in range(node+1)]
visit = [0] * (node+1)
path = []

for i in range(edge):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def bfs(n):
    queue = deque()
    queue.append(n)
    
    while queue :
        n = queue.popleft()
        visit[n] = 1
        path.append(n)

        for i in range(1, node+1):
            if visit[i] == 0 and graph[n][i] == 1 and queue.count(i) <= 0 :
                queue.append(i)

    return len(path) - 1 # 처음 시작노드 제외

print(bfs(int(1)))