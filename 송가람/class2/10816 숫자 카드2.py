import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))

M = int(input())
find = list(map(int, input().split()))

dict = Counter(nums)

answer = []
for num in find:
    answer.append(dict[num])

print(*answer)


# 이분할려고 했지만 실패!
# nums.sort()
# start = 0
# end = len(nums) - 1
# ans = []
# for i in range(M):
#     while start <= end:
#         mid = (start + end) // 2
#         cnt = 0
#         if find[i] == nums[mid]:
#             cnt += 1
#         elif find[i] >= nums[mid]:
#             start = mid + 1
#         else:
#             end = mid - 1
#     ans.append(cnt)    

# print(ans)
