import math
from sys import stdin
input = stdin.readline

n = int(input())
l = set(map(int, input().split()))
result = 0

def check(x) :
    if x == 1 : return False
    for i in range(2, int(math.sqrt(x)) + 1) :
        if x % i == 0 : return False
    return True

for i in l :
    if check(i) : result += 1

print(result)
