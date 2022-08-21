import heapq
import sys
input = sys.stdin.readline
n, bag = map(int, input().split())
jew = []
for i in range(n):
    heapq.heappush(jew, list(map(int, input().split())))

bag_w = [int(input()) for _ in range(bag)]
bag_w.sort()
max_price = []
ans = 0

for w in bag_w:
    while jew and w >= jew[0][0]:
        heapq.heappush(max_price, -heapq.heappop(jew)[1])

    if max_price:
        ans -= heapq.heappop(max_price)
    elif not jew:
        break
    
print(ans)


# 시간초과!!!!!!!
# n, bag = map(int, input().split())
# j = []
# for i in range(n):
#     j.append(list(map(int, input().split())))
# j.sort(key=lambda x: (-x[1], x[0]))

# bag_w = [int(input()) for _ in range(bag)]
# bag_w.sort()
# ans = 0
# for i in range(bag):
#     for l in range(len(j)):
#         if bag_w[i] >= j[l][0]:
#             ans += j[l][1]
#             del j[l]
#             break

# print(ans)

