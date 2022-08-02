# 골드 5
# 행복 유치원

n, k = list(map(int, input().split()))

kid = list(map(int, input().split()))
kid.sort()
cost = []

for i in range(n-1):
    cost.append(kid[i+1]-kid[i])

cost.sort()

for y in range(k-1):
    del cost[-1]
print(sum(cost))
