import heapq
import sys
input = sys.stdin.readline

neg = []
pos = []
one = 0
zero = False
for _ in range(int(input())):
    n = int(input())
    if n < 0:
        heapq.heappush(neg, n)
    elif n == 0:
        zero = True
    elif n == 1:
        one += 1
    elif n > 1:
        heapq.heappush(pos, -n)

ans = 0
while len(neg) > 0:
    if len(neg) == 1 and zero:
        break
    elif len(neg) == 1 and not zero:
        ans += heapq.heappop(neg)
        break
    ans += heapq.heappop(neg) * heapq.heappop(neg)

while len(pos) > 0:
    if len(pos) == 1:
        ans -= heapq.heappop(pos)
        break
    ans += heapq.heappop(pos) * heapq.heappop(pos)

print(ans + one)
