n = int(input())
length = len(str(n))
ans = n
for i in range(1, length - 1):
    ans += (9 * (10 ** i)) * i

ans += ((n + 1) - (10 ** (length - 1))) * (length - 1)

print(ans)