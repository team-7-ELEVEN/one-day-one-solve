n, k = map(int, input().split())
value = [int(input()) for _ in range(n)]
value.sort()
dp = [0] * (k + 1)

# 초기 dp 세팅
for i in range(k + 1):
    if i % value[0] == 0:
        dp[i] = 1


for j in range(1, n):
    v = value[j]
    for k in range(2, k + 1):
        if k - v >= 0:
            dp[k] += dp[k - v]

print(dp[k])