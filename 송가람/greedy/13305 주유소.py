n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
price.pop()

ans = 0
min_p = 1000000000
for d, p in zip(distance, price):
    if min_p > p:
        min_p = p
        ans += min_p * d
    else:
        ans += min_p * d

print(ans)