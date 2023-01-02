n = int(input())

nums = list(map(int, input().split()))

nums.sort()
answer = []
total = 0
for i in nums:
    total += i
    answer.append(total) 

print(sum(answer))