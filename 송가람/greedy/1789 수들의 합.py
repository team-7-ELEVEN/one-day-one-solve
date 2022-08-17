# 뺏을 때 0이상인지 아닌지 검증하기
n = int(input())
cnt = 0
if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    while n > 0: 
        cnt += 1
        n -= cnt
    if n == 0:
        print(cnt)
    else:
        print(cnt-1)