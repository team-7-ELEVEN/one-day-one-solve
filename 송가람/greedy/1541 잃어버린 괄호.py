arr = input().split("-")
split_minus = []
for i in arr:
    split_minus.append(list(map(int, i.split("+"))))

spilt_plus = [sum(i) for i in split_minus]

first = spilt_plus[0]
for i in range(1, len(spilt_plus)):
    first -= spilt_plus[i]

print(first)