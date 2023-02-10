# 코드너무 더러움......
import copy
N = int(input())

board = [list(input()) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def contiguous(arr, s, idx):
    cp_arr = arr.copy()
    if switch_l:
        origin = cp_arr[idx]
        cp_arr[idx] = s
        cp_arr[idx - 1] = origin
    elif switch_r:
        origin = cp_arr[idx]
        cp_arr[idx] = s
        cp_arr[idx + 1] = origin
    else:
        cp_arr[idx] = s
    pre = cp_arr[0]
    cnt = 0
    max_n = 0
    for i in cp_arr:
        if pre == i:
            cnt += 1
        else:
            pre = i
            cnt = 1
        if cnt > max_n:
            max_n = cnt
    return max_n


cnt = 0
max_n = 0

for x in range(N):
    max_c = max(set(board[x]), key = board[x].count)
    if board[x].count(max_c) == N:
        max_n = N
        break
    else:
        for y in range(N):
            for i in range(4):
                switch_l = False
                switch_r = False
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if i == 0:
                        switch_l = True
                    elif i == 1:
                        switch_r = True
                    result = contiguous(board[x], board[nx][ny], y)
                    if max_n < result:
                        max_n = result

switch_board = []
arr = []
for j in range(N):
    for k in range(N):
        arr.append(board[k][j])
    switch_board.append(arr)
    arr = []

for x in range(N):
    for y in range(N):
        for i in range(4):
            switch_l = False
            switch_r = False
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if i == 0:
                    switch_l = True
                elif i == 1:
                    switch_r = True
                result = contiguous(switch_board[x], switch_board[nx][ny], y)
                if max_n < result:
                    max_n = result


print(max_n)


    
                    