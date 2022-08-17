tables = []
n = int(input())
for _ in range(n):
    tables.append(list(map(int, input().split())))

tables.sort(key = lambda x: x[0])
tables.sort(key = lambda x: x[1])

arr = []
cnt = 1
end = tables[0][1]
for i in range(1, n):
    if tables[i][0] >= end:
        cnt += 1
        end = tables[i][1]
print(cnt)