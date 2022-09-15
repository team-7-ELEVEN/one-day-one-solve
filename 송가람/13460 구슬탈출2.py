# from collections import deque
# n, m = map(int, input().split())

# board = [list(input()) for _ in range(n)]

# r_idx = []
# b_idx = []

# dy = [0, 0, -1, 1]
# dx = [1, -1, 0, 0]

# def bfs():
#     r, b = deque()
#     r.append([r_idx[0], r_idx[1]])
#     b.append([b_idx[0], b_idx[1]])
#     while r:
#         y, x = r.popleft()

#         if r[y][x] == "O":
#             print(cnt1, cnt2)
#         elif b[y][x] == "O":
#             -1
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if 0 < ny < n and 0 < nx < m and board[ny][nx] == ".":
            
#                 r.append([ny, nx, i])
#                 board[ny][nx] = " "


# for i in range(1, n - 1):
#     for j in range(1, m - 1):
#         if board[i][j] == "R":
#             r_idx(i, j)
#         elif board[i][j] == "B":
#             b_idx(i, j)




        

