n, m = map(int, input().split())
ans = ''
dna = [input() for _ in range(n)]

cnt = 0
for i in range(m):
    arr = []
    count_list = []
    for j in range(n):
        arr.append(dna[j][i])

    a, c, g, t = 0, 0, 0, 0
    for x in arr:
        if x == 'A':
            a += 1
        elif x == 'C':
            c += 1
        elif x == 'G':
            g += 1
        elif x == 'T':
            t += 1
        
    max_d = max(a, c, g, t)
    if max_d == a:
        ans += 'A'
        cnt += c + g + t
    elif max_d == c:
        ans += 'C'
        cnt += a + g + t
    elif max_d == g:
        ans += 'G'
        cnt += a + c + t
    elif max_d == t:
        ans += 'T'
        cnt += a + c + g

print(ans)
print(cnt)