N, M, B = map(int, input().split())
ground = []
for _ in range(N):
    for i in list(map(int, input().split())):
        ground.append(i)

ground.sort()

add = 0
discard = 0

# 일단 포기!
    