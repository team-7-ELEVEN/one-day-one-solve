n, k = map(int, input().split())
idx = 0
ans = []
arr = [i for i in range(1, n + 1)]

while len(arr) >= 1:
    out = (idx + (k - 1)) % len(arr)
    ans.append(arr.pop(out))
    idx = out


print("<", end="")
print(*ans, sep=", ", end="")
print(">")
