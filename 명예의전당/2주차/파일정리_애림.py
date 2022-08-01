# 파일 정리

import sys
from collections import defaultdict

n = int(sys.stdin.readline())
result = defaultdict(int)

for _ in range(n):
    file = sys.stdin.readline().strip().split('.')
    result[file[1]] += 1

result = sorted(result.items())

for x, y in result:
    print(x, y)
