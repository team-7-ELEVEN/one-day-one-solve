import sys
from collections import Counter

input = sys.stdin.readline
# 상근이가 가지고 있는 카드의 갯수
N = int(input())
# 숫자카드에 적혀있는 정수
card = list(map(int,input().split()))
M = int(input())
# 상근이가 몇개 가지고 있는 숫자카드인지 구해야할 M개의 정수
check_list = list(map(int,input().split()))

card_1 = Counter(card)
sol = []
for i in check_list:
    sol.append(card_1[i])

print(*sol)