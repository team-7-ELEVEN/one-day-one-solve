from sys import stdin
input = stdin.readline

n = int(input())
p = []
for _ in range(n) :
    x, y = map(int, input().split())
    p.append((x,y))

for x, y in p :
    rank = 1
    for i, j in p :
        if x < i and y < j : # 나보다 큰 사람 생기면 순위 밀림
            rank += 1
    print(rank, end=" ")