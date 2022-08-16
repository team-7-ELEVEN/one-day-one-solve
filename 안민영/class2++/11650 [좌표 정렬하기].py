import sys
input = sys.stdin.readline

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

l.sort()

for x, y in l :
    print(x, y)