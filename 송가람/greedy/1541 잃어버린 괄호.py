arr = input().split("-")
split_minus = []
for i in arr:
    split_minus.append(list(map(int, i.split("+"))))

split_plus = [sum(i) for i in split_minus]

first = split_plus[0]
for i in range(1, len(split_plus)):
    first -= split_plus[i]

print(first)