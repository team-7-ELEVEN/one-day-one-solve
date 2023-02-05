import sys
input = sys.stdin.readline
N, M = map(int, input().split())

board = [[0] * (M + 1)]

for _ in range(N):
    board.append([0] + list(map(int, input().split())))

K = int(input())

summing = []
for _ in range(K):
    i, j, x, y = map(int, input().split())
    for X in range(i, x + 1):
        summing.append(sum(board[X][j: y + 1]))
    print(sum(summing))
    summing = []



