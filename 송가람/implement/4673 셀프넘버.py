nums = []

for i in range(1, 10000):
    str_n = str(i)
    d = i
    for n in str_n:
        
        d += int(n)
    nums.append(d)
    d = 0

set_nums = set(nums)

for i in range(1, 10000):
    if i not in set_nums:
        print(i)