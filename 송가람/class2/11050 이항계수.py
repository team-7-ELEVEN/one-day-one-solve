from itertools import combinations
n, k = map(int, input().split())
comb = list(combinations(list(range(1, n+1)), k))
print(len(comb))
