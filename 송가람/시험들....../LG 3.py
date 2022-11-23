from collections import deque
q = deque(['o', 'w', 'w', 'o', 'w', 'w'])
ans = []
cnt = 1
pre = q[0]
for i in range(1, len(q)):
    if pre != q[i]:
        pre = q[i]
        ans.append(cnt)
        cnt = 1
    else:
        cnt += 1
    
print(ans)