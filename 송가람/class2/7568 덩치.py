N = int(input())
arr = []
ans = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    cnt = 0
    for j in range(N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    ans.append(cnt + 1)

for i in ans:
    print(i, end=" ")


