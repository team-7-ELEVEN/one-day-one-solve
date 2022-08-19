from collections import Counter
import sys
input = sys.stdin.readline

def check(h) :
    result = 0
    for l in land : # land = {0: 11, 1: 1, ...}
        # h 높이보다 낮은 경우, 블럭 올리기
        if l < h :
            result += land[l] * (h - l)
        # h 높이보다 높은 경우, 블럭 제거하고 인벤에 넣기
        else :
            result += land[l] * (l - h) * 2

    return result

n, m, b = map(int, input().split())
matrix = []
for _ in range(n) :
    matrix += list(map(int, input().split()))


land = dict(Counter(matrix))
height, time = 0, 100000000000000
total = sum(matrix)

for h in range(257) :

    # (결과적으로 쌓일 전체 블록)보다 (현재 블록과 인벤토리 블록)이 더 많을 때만 계산하기
    if n * m * h <= total + b :
        t = check(h)
        if time >= t :
            height = h
            time = t

print(time, height)