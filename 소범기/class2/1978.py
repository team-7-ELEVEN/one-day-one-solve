import sys
import math

input = sys.stdin.readline

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True 

N = int(input())

data = list(map(int,input().split()))
cnt = 0
for i in data:
    if is_prime(i) == True:
        cnt+=1

print(cnt)