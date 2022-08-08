n = int(input())
stk, ans = [], []
pre = 0
find = True

for _ in range(n):
    now = int(input())
    if now >= pre:
        for i in range(pre+1, now+1):
            stk.append(i)
            ans.append("+")
        pre = now
        stk.pop()
        ans.append("-")
    elif stk[-1] > now:
        find = False
    else:
        stk.pop()
        ans.append("-")

if not find:
    print("NO")
else:
    for i in ans:
        print(i)
        


