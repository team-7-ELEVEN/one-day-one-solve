S = input()

ans = ""
reverse = ""
tag = False
for s in S:
    if s == ' ':
        ans += reverse[::-1] + ' '
        reverse = ''
        continue
    elif s == '<':
        tag = True
        if reverse:
            ans += reverse[::-1]
            reverse = ''
    elif s == '>':
        tag = False
        ans += '>'
        continue
    if tag:
        ans += s
    else:
        reverse += s

ans += reverse[::-1]
print(ans)

