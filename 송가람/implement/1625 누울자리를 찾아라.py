n = int(input())
board = [list(input()) for _ in range(n)]

def can_lie():
    horizontal = 0
    vertical = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if board[i][j] == '.':
                cnt += 1
            else:
                if cnt >= 2:
                    horizontal += 1
                cnt = 0
        if cnt >= 2:
            horizontal += 1
    
    for i in range(n):
        cnt = 0
        for j in range(n):
            if board[j][i] == '.':
                cnt += 1
            else:
                if cnt >= 2:
                    vertical += 1
                cnt = 0
        if cnt >= 2:
            vertical += 1

    return horizontal, vertical

h, v = can_lie()
print(h, v)