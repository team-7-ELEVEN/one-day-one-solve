import sys
input = sys.stdin.readline

def is_bingo():
    cnt = 0
    cross = 0
    for i in range(5):
        vertical = 0
        if sum(bingo[i]) == 0:
            cnt += 1
        for j in range(5):
            vertical += bingo[j][i]
            if j == i:
                cross += bingo[j][i]
        if vertical == 0:
            cnt += 1
    if cross == 0:
        cnt += 1
    if (bingo[0][4] + bingo[1][3] + bingo[2][2] + bingo[3][1] + bingo[4][0]) == 0:
        cnt += 1
    return True if cnt >= 3 else False

bingo = [list(map(int, input().split())) for _ in range(5)]

nums = []
flag = False
for _ in range(5):
    nums += list(map(int, input().split()))

for i in range(len(nums)):
    for j in range(5):
        if nums[i] in bingo[j]:
            bingo[j][bingo[j].index(nums[i])] = 0
            break
    flag = is_bingo()
    if flag:
        print(i + 1)
        break
