import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = [int(input()) for _ in range(n)]
heapq.heapify(heap)
comb = 0
ans = 0
while len(heap) > 1:
    comb = heapq.heappop(heap) + heapq.heappop(heap)
    ans += comb
    heapq.heappush(heap, comb)

print(ans)