import math
rest = [0] * 10
six_and_nine = 0

for i in input():
    if i == '6' or i == '9':
        six_and_nine += 1
    else:
        rest[int(i)] += 1

max_nums = max(rest)
min_six_nine = math.ceil(six_and_nine / 2) 

print(six_and_nine)
print(rest)

if max_nums > min_six_nine:
    print(max_nums)
else:
    print(min_six_nine)