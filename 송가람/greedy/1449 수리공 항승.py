import heapq
n, l = map(int, input().split())
pipe = list(map(int, input().split()))
pipe.sort()

ans = 0
idx = 0
while pipe:
    if idx < len(pipe):
        if pipe[idx] < pipe[0] + l:
            idx += 1
        else:
            pipe = pipe[idx:]
            idx = 0
            ans += 1
    else:
        pipe = []
        ans += 1
    

# 실패!
# import heapq
# n, l = map(int, input().split())
# heap = list(map(int, input().split()))
# heapq.heapify(heap)

# cnt = 0
# cur = heapq.heappop(heap)
# ans = 0
# while len(heap) > 0: 
#     cnt += 1
#     cur += 1
#     if cnt == l:
#         ans += 1
#         cnt = 0
#         while True:
#             if heap:
#                 if cur > heap[0]:
#                     heapq.heappop(heap)
#                 else:
#                     break
#             else:
#                 break  
# print(ans)