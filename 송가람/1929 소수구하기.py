M, N = map(int, input().split())
ans = []
cnt = 0
nums = list(range(M, N+1))

for num in nums:
    check = True
    sqrt = int(num ** (1/2))
    if num == 1:
        check = False
    elif num > 2:
         for i in range(2, sqrt + 2):
            if num % i == 0:
                check = False
                break
    if check:
        print(num)