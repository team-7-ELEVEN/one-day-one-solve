import sys
input = sys.stdin.readline

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

l.sort(key = lambda x : (x[1], x[0]))

for x, y in l :
    print(x, y)