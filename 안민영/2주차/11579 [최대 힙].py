import sys
import heapq as hq

input = sys.stdin.readline

num = int(input())
max_heap = []

for i in range(num) :
    n = int(input())
    if n == 0 :
        if len(max_heap) <= 0 :
            print(0)
        else : 
            print(hq.heappop(max_heap)[1])
    else :
        hq.heappush(max_heap, (-n, n))