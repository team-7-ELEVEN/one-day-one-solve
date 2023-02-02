board = [[0] * 100 for _ in range(100) ]
n = int(input())

def board_check(x, y):
    end = y + 10 
    while y < end:
        for i in range(x, x + 10):
            board[y][i] = 1
        y += 1

for _ in range(n):
    x, y = map(int, input().split())
    board_check(x, y)

cnt = 0
for j in board:
    for k in j:
        if k == 1:
            cnt += 1 

print(cnt)