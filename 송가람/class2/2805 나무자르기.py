# 시간 초과 => 자른 나무의 개수가 필요한 개수를 넘으면 break 조건 걸어주기
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

trees = list(map(int, input().split()))

trees.sort()
start = 1
end = trees[-1]

while start <= end:
    mid = (start + end) // 2
    cutting = 0
    for i in trees:
        if i > mid:
            cutting += i - mid
        if cutting > M:
            break
    if cutting >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)