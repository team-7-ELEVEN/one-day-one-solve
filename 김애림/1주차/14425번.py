# 문자열 집합
# 실버 3

import sys
N, M = map(int, sys.stdin.readline().split())

s = set(input() for _ in range(N))
count = 0
for _ in range(M):
    string = input()
    if string in s:
        count += 1

print(count)
