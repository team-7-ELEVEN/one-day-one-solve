t=int(input())

for _ in range(t):
    stack=[]
    string=input()
    flag=False
    for s in string:
        if s=='(':
            stack.append(s)
        else:
            if len(stack)==0:
                print('NO')
                flag=True
                break
            # 밑의 if문 제거하고 stack.pop()만 해도 가능
            if stack[-1]=='(':
                stack.pop(-1)
            else:
                stack.append(s)
    if flag==True:
        flag==False
        continue
    if len(stack)!=0:
        print('NO')
    else:
        print('YES')
