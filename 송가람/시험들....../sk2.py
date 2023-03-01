from collections import deque

def solution(p, b):
    answer = []
    board = [[] for _ in range(len(p))]
    for i in range(len(p)):
        if p[i] == -1:
            continue
        board[i].append(p[i])
        board[p[i]].append(i)
    

    def bfs(start):
        q = deque()
        chk = [False] * (len(p))
        chk[start] = True
        q.append(start)
        while q:
            node = q.popleft()
            for i in board[node]:
                if not chk[i]:
                    chk[i] = True
                    q.append(i)
        return chk.count(True)

    for j in b:
        if p[j] != -1:
            answer.append(0)
        else:
            answer.append(bfs(j))

    return answer

print(solution(

[2, 2, -1, 1, 5, -1, 5], [1, 5]))



ans = []



# print(bfs(a))