from collections import Counter
import sys
input = sys.stdin.readline
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

# 산술평균
mean = sum(nums) / N
print(round(mean))

# 중앙값
nums.sort()
mid = nums[int(N / 2)]
print(mid)

# 최빈값
counts = Counter(nums)
fre = counts.most_common()
max_fre = fre[0][1]
max_nums = []
for i in fre:
    if i[1] == max_fre:
        max_nums.append(i[0])

if len(max_nums) > 1:
    print(max_nums[1])
else:
    print(max_nums[0])

# 범위
print(nums[-1] - nums[0])

