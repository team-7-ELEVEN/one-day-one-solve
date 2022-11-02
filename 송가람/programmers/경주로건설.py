from collections import deque
q = deque()

## 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def solution(board):

    l = len(board)
    def bfs(start):
        q.append(start)
        while q:
            y, x, d = q.pop()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < l and 0 <= nx < l:
                    
