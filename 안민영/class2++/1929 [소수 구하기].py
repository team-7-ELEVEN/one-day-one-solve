import math
from sys import stdin
input = stdin.readline

min, max = list(map(int, input().split()))
x = min

# 시간 초과
'''
def check(x) :
    for i in range(2, x) :
        if x % i == 0 :
            return False
    return True 
'''

def check(x) :
    if x == 1 : return False

    for i in range(2, int(math.sqrt(x)) + 1) :
        if x % i == 0 :
            return False
    return True

while x <= max :
    if check(x) : print(x)
    x += 1