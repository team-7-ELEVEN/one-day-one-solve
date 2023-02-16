N, K = map(int, input().split())

medal = []

for _ in range(N):
    k = list(map(int, input().split())) 
    if k[0] == K:
        base = k
    medal.append(k)

medal.sort(key=lambda x: (-x[1], -x[2], -x[3]))
idx = medal.index(base)

for i in range(N):
    if medal[idx][1:] == medal[i][1:]:
        print(i + 1)
        break
