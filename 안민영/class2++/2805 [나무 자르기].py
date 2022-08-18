from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, max(trees)

while start <= end :
    total = 0
    mid = (start + end) // 2

    # 자른 나무들 총 합
    for tree in trees :
        if tree > mid :
            total += tree - mid

    # 자른 나무들 총 합이 목표값(m) 이상인 경우 (오른쪽 부분 탐색)
    if total >= m :
        start = mid + 1
    # 자른 나무들 총 합이 목표값(m)보다 적은 경우 (왼쪽 부분 탐색)
    else :
        end = mid - 1

print(end)