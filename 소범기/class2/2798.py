from itertools import combinations
N,M = list(map(int,input().split()))
data = list(map(int,input().split()))
big_sum = 0
for card in combinations(data,3):
    temp = sum(card)
    if big_sum < temp <= M:
        big_sum = temp
print(big_sum)