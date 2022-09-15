n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

chk = [False] * n
def dfs(y):
    for i in range(n):
        if graph[y][i] == 1 and not chk[i]:
            chk[i] = True
            dfs(i)

for i in range(n):
    dfs(i)

    for j in range(n):
        if chk[j]:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    chk = [False] * n        


