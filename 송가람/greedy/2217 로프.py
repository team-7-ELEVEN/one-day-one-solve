n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort(reverse=True)
ans = []
for i in range(1, n+1):
    ans.append(rope[i-1] * i)

print(max(ans))
