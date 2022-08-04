from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.reverse()
tmp = k
cnt = 0

for coin in coins:
    if tmp < coin:
        continue

    cnt += tmp // coin
    tmp -= coin * (tmp // coin)

    if tmp == 0:
        print(cnt)
        break

# reverse reversed
# https://itholic.github.io/python-reverse-reversed/
