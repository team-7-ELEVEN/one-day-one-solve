import sys
input=sys.stdin.readline

n,m=map(int,input().split())
set_s=[]
cnt=0

for _ in range(n):
    set_s.append(input())

for _ in range(m):
    string=input()
    if string in set_s:
        cnt+=1
print(cnt)


# set_s를 set()으로 만들어도 됨
