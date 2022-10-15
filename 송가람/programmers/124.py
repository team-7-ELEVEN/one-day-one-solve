def solution(n):
    nums = ["1", "2", "4"]
    N = 0
    cnt = 3
    if n <= 3:
        return nums[n - 1]
    
    while True:
        for i in range(N, N+3):
            for j in ["1", "2", "4"]:
                nums.append(nums[i] + j)
                cnt += 1
                if n == cnt:
                    return nums[n - 1]
                    break
        N += 3

print(solution(13))