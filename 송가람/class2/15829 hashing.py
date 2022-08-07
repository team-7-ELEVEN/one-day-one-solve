n = int(input())
str = list(input())
ans = 0
M = 1234567891
for i,j  in zip(range(n), str):
        ans += ((ord(j) - 96 ) * (31**i))

if ans > M:
    print(ans % M)
else:
    print(ans)


