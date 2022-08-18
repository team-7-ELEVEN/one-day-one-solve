import sys
input = sys.stdin.readline

k, n = map(int, input().split()) # 랜선의 개수, 필요한 랜선의 개수
m = [int(input()) for _ in range(k)] # 랜선의 길이

start, end = 1, max(m)

while start <= end :
    total = 0
    mid = (start + end) // 2

    for i in m : 
        total += i // mid

    if total >= n :
        start = mid + 1
    else :
        end = mid - 1

print(end)