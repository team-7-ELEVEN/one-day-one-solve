n, m = map(int, input().split())
height = list(map(int, input().split()))

ans = 0
for i in range(1, m-1):
    right_max = max(height[:i])
    left_max = max(height[i + 1:])

    h = min(right_max, left_max)
    if h > height[i]:
        ans += h - height[i]
print(ans)

