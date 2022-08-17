import sys
import math
input = sys.stdin.readline
N,M,B1 = list(map(int,input().split()))

data = [list(map(int,input().split())) for _ in range(N)]

h_max = max(max(data))
h_min = min(min(data))

min_t = math.inf
B_min = B1
for i in range(h_max,h_min-1,-1):
    t=0
    B=B1
    for x in range(N):
        for y in range(M):
            if data[x][y] > i:
                iter_ = data[x][y]-i
                B += iter_
                t += iter_*2
            # 추가작업
            else:
                iter_ = i-data[x][y]
                B -= iter_
                t += iter_
    if B < 0:
        continue
    if min_t > t:
        min_t = t
        min_i = i
        

print(min_t,min_i)