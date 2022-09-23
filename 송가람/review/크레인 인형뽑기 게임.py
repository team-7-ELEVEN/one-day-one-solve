from collections import deque
def solution(board, moves):
    q = deque()
    moves = deque(moves)
    cnt = 0
    while moves:
        idx = moves.popleft()
        for i in range(len(board)):
            pick = board[i][idx - 1]
            if pick != 0:
                if q:
                    if q[-1] == pick:
                        q.pop()
                        cnt += 2
                        board[i][idx - 1] = 0
                        break
                q.append(pick)       
                board[i][idx - 1] = 0
                break
    
    return cnt