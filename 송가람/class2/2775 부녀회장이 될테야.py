# 범기가 도와줬슴,,,복습하자!

import sys
input = sys.stdin.readline
N = int(input())

for _ in range(N):
    k = int(input())
    n = int(input())

    init_floor = [i for i in range(1, n + 1)]

    for _ in range(k):
        cur_floor = []
        for i in range(1, n + 1):
            cur_floor.append(sum(init_floor[:i]))  
        init_floor = cur_floor
    print(init_floor[n-1])
