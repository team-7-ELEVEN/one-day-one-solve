N, K = map(int, input().split())
nums = list(range(2, N+1))

idx = 0
order = []
m = 1
while idx < len(nums):
    m = nums[idx]
    while idx < len(nums):
        start = nums[idx]
        if start % m == 0:
            order.append(start)
            nums.remove(start)
            continue
        idx += 1
    idx = 0

print(order[K - 1]) 


