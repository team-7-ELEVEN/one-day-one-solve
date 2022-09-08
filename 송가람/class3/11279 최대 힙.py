import heapq
import sys
input = sys.stdin.readline
heap = []

for i in range(int(input())):
    inpt = int(input())
    heapq.heappush(heap, -inpt)
    if inpt == 0:
        if heap:
            hqpop = heapq.heappop(heap)
            print(-hqpop)
        else:
            print(0)
