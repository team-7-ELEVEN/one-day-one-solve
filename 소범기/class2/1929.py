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

M,N = list(map(int,input().split()))

for i in range(M,N+1):
    if is_prime(i)==True:
        print(i)
