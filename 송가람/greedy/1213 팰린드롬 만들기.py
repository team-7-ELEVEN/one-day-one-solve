word = input()
# cnt = 0
# pre = None
# mid = None
dic = {}
for i in word:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

dic = sorted(dic.items())
mid = ""
ans = ""
for v,k in dic:
    if k % 2 == 1:
        if len(mid) > 0:
            print("I'm Sorry Hansoo")
            break
        mid = v
    
    ans += v * int(k // 2)
else:
    print(ans + mid + ans[::-1])
    
