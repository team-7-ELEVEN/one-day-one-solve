# 괄호
# 9012번

import sys

N = int(input())

for _ in range(N):
    x = sys.stdin.readline().strip()
    result = 0
    for i in x:
        if i == "(":
            result = result + 1
        else:
            result = result - 1
        if result < 0:
            break
    if result == 0:
        print("YES")
    else:
        print("NO")
