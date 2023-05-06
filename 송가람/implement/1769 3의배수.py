n = input()
cnt = 0
while True:
    a = 0
    if len(n) == 1: 
        if n == '3' or n == '6' or n == '9':
            print(cnt)
            print("YES")
            break
        else:
            print(cnt)
            print("NO")
            break
    else:
        for i in n:
            a += int(i)
        n = str(a)
        cnt += 1


