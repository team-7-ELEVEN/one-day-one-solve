# 맞은 풀이
N, K = map(int, input().split())
arr = [int(input()) for i in range(N)]
count = 0
coin = -1
while K > 0:
    count += K//arr[coin]
    K %= arr[coin]
    coin -= 1
print(count)

# 시간초과

# N, K = map(int, input().split())
# arr = [int(input()) for i in range(N)]
# arr.sort()
# count, coin = 0, -1
# while K > 0:
#     if arr[coin] > K:
#         coin -= 1
#     else:
#         count += 1
#         K -= arr[coin]
# print(count)
