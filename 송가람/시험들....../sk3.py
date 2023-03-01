from collections import deque
def solution(boards):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0] 
    answer = []
        

    # def dfs(y, x, cnt):
    #     if cnt == one - 1:
    #         return cnt
    #     boards[y][x] = '0'
    #     for i in range(4):
    #             ny = y + dy[i]
    #             nx = x + dx[i]
    #             if 0 <= ny < len(boards) and 0 <= nx < len(boards):
    #                 if boards[ny][nx] == '1':
    #                     cnt += 1
    #                     return dfs(ny, nx, cnt)

#     def bfs():
#         q = deque()
#         q.append([y, x, cnt])
#         boards[y][x] = '0'
#         while q: 
#             y, x, cnt = q.popleft()
#             if max_c < cnt:
#                 max_c = cnt
#             for i in range(4):
#                 ny = y + dy[i]
#                 nx = x + dx[i]
#                 if 0 <= ny < len(boards) and 0 <= nx < len(boards):
#                     if boards[ny][nx] == '1':
#                         boards[ny][nx] = '0'
#                         q.append([ny, nx, cnt + 1])
#         return max_c

#     for l in range(len(boards)):
#         boards[l] = list(boards[l])
#     one = 0
#     for i in range(len(boards)):
#         for j in range(len(boards)):
#             if boards[i][j] == '1':
#                 one += 1
#             elif boards[i][j] == '2':
#                 d_i, d_j = i, j

#     bfs(d_i, d_j, 1)


# print(solution(["00011", "01111", "21001", "11001", "01111"]))
