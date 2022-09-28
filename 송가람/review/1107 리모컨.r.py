n = int(input())
m = int(input())

ans = abs(100 - n)
if m:
    broken = list(input().split())
else:
    broken = []

for i in range(1000000):
    for j in str(i):
        if j in broken:
            break
    else:
        ans = min(ans, (len(str(i)) + abs(n - i)))

print(ans)
    