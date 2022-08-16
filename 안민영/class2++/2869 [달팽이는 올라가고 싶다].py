import math
from sys import stdin
input = stdin.readline

a, b, v = list(map(int, input().split()))

'''
meter = 0
day = 1
while True : 
    meter += a

    if meter >= v :
        print(day)
        break
    else :
        meter -= b
        day += 1
'''

day = math.ceil((v-b) / (a-b))

print(day)