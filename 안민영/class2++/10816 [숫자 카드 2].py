import sys
input = sys.stdin.readline

n = int(input()) # 상근이가 가지고 있는 숫자 카드 개수
nums = list(map(int, input().split()))

m = int(input()) 
check_nums = map(int, input().split())

# 시간 초과
'''
for x in check_nums :
    print(nums.count(x), end=' ')
'''

# Counter 사용 시
'''
from collections import Counter

cards = Counter(nums)
result = []
for i in check_nums:
    result.append(cards[i])

print(*result)
'''

# Dictionary 사용 시
from collections import defaultdict

dic = defaultdict(int)

for i in nums :
    dic[i] += 1

for i in check_nums :
    if i in dic :
        print(dic[i], end=' ')
    else :
        print(0, end=' ')