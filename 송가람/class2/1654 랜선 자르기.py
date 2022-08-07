# 이분탐색
K, N = map(int,input().split())
lan = []

for i in range(K):
    lan.append(int(input()))

lan.sort()
start = 1
end = lan[-1]

while start <= end:
    mid = (start + end) // 2
    num = 0
    for i in lan:
        num += ( i // mid )
        
    if num >= N:
      
        start = mid + 1

    else:
        end = mid - 1

print(end)


# 완전탐색의 경우

# K, N = map(int,input().split())
# cnt = 1
# num = 0
# lan = []

# for i in range(K):
#     lan.append(int(input()))

# while True:
#     for i in lan:
#         num = ( i // cnt ) + num
        
#     if num >= N:
#         num = 0
#         cnt += 1
#     else:
#         print(cnt-1)
#         break
