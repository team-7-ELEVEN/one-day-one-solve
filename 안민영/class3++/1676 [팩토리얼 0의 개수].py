from math import factorial
import sys
input = sys.stdin.readline

n = int(input())
n = str(factorial(n))
n = n[::-1]
cnt = 0

for i in n :
    if i == '0' : cnt += 1
    else :
        print(cnt)
        break