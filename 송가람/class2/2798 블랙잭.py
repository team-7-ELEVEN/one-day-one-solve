import itertools

n, M = map(int, input().split())
arr = list(map(int, input().split()))
result = list(map(list, itertools.combinations(arr,3)))
sum_list = []

for i in result:
    total = sum(i)
    if total <= M:
        sum_list.append(total)

print(max(sum_list))


