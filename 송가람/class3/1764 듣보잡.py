h, s = map(int, input().split())

h_and_s = {}
for _ in range(h + s):
    inpt = input()
    if inpt in h_and_s:
        h_and_s[inpt] += 1
    else:
        h_and_s[inpt] = 1

sorted = sorted(h_and_s.items())
ans = []
for i in sorted:
    if i[1] > 1:
        ans.append(i[0])
        
print(len(ans))
for j in ans:
    print(j)

