from sys import stdin
input = stdin.readline

# 메모리 초과
'''
n = int(input())
l = [input().strip() for _ in range(n)]
l.sort()

for i in l :
    print(i)
'''

nums = [0 for _ in range(10001)]
n = int(input())
for _ in range(n) :
    x = int(input())
    nums[x] += 1

for i in range(len(nums)) :
    if nums[i] != 0 : 
        for _ in range(nums[i]) :
            print(i)
    else : continue