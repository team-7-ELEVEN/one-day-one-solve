N, M = map(int, input().split())

min_n = min(N, M)

board = [list(input()) for i in range(N)]

def square_area(x, y):
    n = 1
    max_area = 1
    vertex = board[x][y]
    while n < min_n:
        if x + n < N and y + n < M:
            if vertex == board[x][y + n] and vertex == board[x + n][y] and vertex == board[x + n][y + n]:
                max_area = (n + 1)**2
                
        n += 1

    return max_area

max_area = 1
for i in range(N):
    for j in range(M):
        area = square_area(i, j)
        if area > max_area:
            max_area = area

print(max_area)
