N = int(input())
A = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

A.sort()

def search_num(num):
    start = 0
    end = len(A) - 1
    while start <= end:
        mid = ( start + end ) // 2
           
        if num == A[mid]:
            return 1
        if num > A[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return 0

for num in nums:
   print(search_num(num))

        