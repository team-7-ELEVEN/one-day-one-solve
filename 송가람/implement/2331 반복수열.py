A, P = map(int, input().split())
n = [A]
while True:
    s = 0
    for i in str(A):
        s += int(i) ** P
    if s in n:
        break
    else:
        n.append(s)
        A = s
ans = len(n[:n.index(s)])
print(ans)