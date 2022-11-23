def solution(edges, roots):
    n = len(edges) + 1
    ans = [0] * (n - 1)
    curr_e = edges
    graph = [[] for _ in range(n + 1)]
    for i in edges:
        a, b = i
        graph[a].append(b)
        graph[b].append(a)
    
    def dfs(root):
        visited[root] = True
        for child in graph[root]:
            if not visited[child]:
                new_e.append([root, child])
                visited[child] = True
                dfs(child)
        

    for root in roots:
        new_e = []
        visited = [False] * (n + 1)
        dfs(root)
        for j in range(n - 1):
            if not curr_e[j] in new_e:
                ans[j] += 1
                curr_e[j] = [curr_e[j][1], curr_e[j][0]]

    return ans

edges = [[1, 3], [1, 2], [2, 4], [2, 5]]
roots = [2, 3]
print(solution(edges, roots))


