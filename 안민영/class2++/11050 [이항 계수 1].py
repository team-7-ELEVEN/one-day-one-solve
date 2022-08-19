import sys
n, k = map(int, sys.stdin.readline().split())
result = 1

for i in range(k) :
    result *= (n-i) / (i+1)
print(int(result))