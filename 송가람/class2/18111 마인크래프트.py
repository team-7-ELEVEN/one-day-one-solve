import math
N, M, B = map(int, input().split())
blocks = []
for _ in range(N):
    for i in list(map(int, input().split())):
        blocks.append(i)

min_t = math.inf
max_h = max(blocks)
min_h = min(blocks)

for h in range(max_h, min_h - 1, -1):
    b = B
    t = 0
    for block in blocks:
        if h > block:
            b -= h - block
            t += h - block
        elif h < block:
            b += block - h
            t += (block - h) * 2

    if b < 0:
        continue

    elif min_t > t:
        min_t = t
        height = h
        
print(min_t, height)