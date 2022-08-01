'''
https://www.acmicpc.net/problem/2512

4
120 110 140 150
485

정해진 총액 이하에서 가능한 한 최대의 총 예산 
- 모든 요청이 배정될 수 있는 겨우 요청한 금액을 그대로 배정한다 
- 모든 요청이 배정될 수 없는 경우 특정한 정수 상한액을 계산하여 그 이상인 예산 요청에 모두 상한액을 배정 
- 상한액 이하의 예산 요청에 대해서는 요청한 금액을 그대로 배정 


'''

import sys


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return mid


n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
m = int(input())

sorted_arr = sorted(arr)
mid = m//n
answer = 0
res = 0
if sum(sorted_arr) < m:
    answer = sorted_arr[-1]
else:
    index = binary_search(sorted_arr, mid, 0, n - 1)
    small_sum = sum(sorted_arr[:index+1])
    remain_arr = sorted_arr[index+1:]
    remain = m - small_sum
    for item in range(mid, remain // len(remain_arr)):


print(answer)
