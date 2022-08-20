n, money = map(int, input().split())

coin = [int(input()) for i in range(n)]
ans = 0

while True:
    for i in reversed(coin):
        ans += money // i
        money = money % i
    if money == 0:
        break
    
print(ans)
