n = input()
nums = []
if n.find("0") == -1:
    print(-1)
else:
    nums = [int(i) for i in n]
    if sum(nums) % 3 == 0:
        nums.sort(reverse=True)
        new_n = "".join(map(str, nums))
        print(int(new_n))
    else:
        print(-1)
