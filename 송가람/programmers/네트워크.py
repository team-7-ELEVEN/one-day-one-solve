from collections import deque

def solution(n, computers):
    q = deque()
    cnt = 0
    
    def bfs(start):
        q.append(start)
        chk[start] = True
        while q:
            node = q.popleft()
            for idx in range(n):
                if computers[node][idx] == 1 and not chk[idx]:
                        q.append(idx)
                        chk[node] = True
                    
    chk = [False] * n
    
    for j in range(n):
        if not chk[j]:
            bfs(j)
            cnt += 1
            
    return cnt