N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int,input().split())))

result = []
for i in data:
    cnt = 1
    for j in data:
        if i[0] < j[0] and i[1] < j[1]:
            cnt+=1
    result.append(cnt)
print(*result)