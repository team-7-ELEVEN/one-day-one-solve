# 최대 힙
# 시간 초과

# n = int(input())
# result = []
# for _ in range(n):
#     x = int(input())
#     if x > 0:
#         result.append(x)
#     else:
#         if result:
#             print(max(result))
#             result.remove(max(result))
#         else:
#             print(0)


# 파이썬에서는 최대힙을 제공 x하므로 부호를 변경하는 방식을 사용하기.

import heapq
import sys
n = int(sys.stdin.readline())

num = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(num, -x)
    else:
        if num:
            print(-heapq.heappop(num))
        else:
            print(0)
