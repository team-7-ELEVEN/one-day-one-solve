from sys import stdin
input = stdin.readline

# 처음 시작 w, b에 따라
# 다시 칠해야하는 개수 구하기
# 최솟값으로 업데이트

def check(row, col) :
    w_count = 0
    b_count = 0
    for x in range(row, row+8) :
        for y in range(col, col+8) :
            # 처음 시작이 W인 경우
            if (x+y) % 2 == 0 and matrix[x][y] != 'W' :
                w_count += 1
            elif (x+y) % 2 == 1 and matrix[x][y] != 'B' :
                w_count += 1

            # 처음 시작이 B인 경우
            if (x+y) % 2 == 0 and matrix[x][y] != 'B' :
                b_count += 1
            elif (x+y) % 2 == 1 and matrix[x][y] != 'W' :
                b_count += 1

    return min(w_count, b_count)


n, m = map(int, input().split())
matrix = [input().strip() for _ in range(n)]
num = 64

for x in range(0, n-7) :
    for y in range(0, m-7) :
        num = min(num, check(x, y))

print(num)