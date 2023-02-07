# 답을 봤음!
b = input()

stack = []
tmp = 1
ans = 0
for i in range(len(b)):
    if b[i] == '(':
        stack.append(b[i])
        tmp *= 2
    elif b[i] == '[':
        stack.append(b[i])
        tmp *= 3
    elif b[i] == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        elif b[i - 1] == '(':
            ans += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == '(':
            ans = 0
            break
        elif b[i - 1] == '[':
            ans += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(ans)




