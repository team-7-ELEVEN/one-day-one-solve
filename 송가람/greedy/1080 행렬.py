n, m = map(int, input().split())
matrix1,matrix2 = [], []

def convert(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            matrix1[x][y] = 1 - matrix1[x][y] 

for _ in range(n):
    matrix1.append(list(map(int, input())))

for _ in range(n):
    matrix2.append(list(map(int, input())))

cnt = 0 
if (n < 3 or m < 3) and matrix1 != matrix2:
    print(-1)
else:
    for i in range(n - 2):
        for j in range(m - 2):
            if matrix1[i][j] != matrix2[i][j]:
                cnt += 1
                convert(i, j)

    if matrix1 != matrix2:
        print(-1)
    else:
        print(cnt)


