n = int(input())
N = 0
ans = 1
curr = 0
while True:
    curr = (6 * N) + curr
    room = 1 + curr
    if n <= room:
        print(ans)
        break
    N += 1
    ans += 1