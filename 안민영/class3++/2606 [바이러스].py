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



'''
import sys
from sys import stdin
sys.setrecursionlimit(10**6)

def dfs(N, i):
    global cnt

    if visited[i]:
        return
    else:
        cnt += 1
        visited[i] = 1
        for ni in adjList[i]:
            dfs(N, ni)

N = int(input())
M = int(input())
adjList = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    adjList[a].append(b)
    adjList[b].append(a)

cnt = 0
dfs(N, 1)
print(cnt-1)
'''
