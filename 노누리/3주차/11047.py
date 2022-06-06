import sys
input=sys.stdin.readline

n,k=map(int,input().split())
cnt=0
coin=[]

for _ in range(n):
    coin.append(int(input()))

coin=sorted(coin,reverse=True)

for c in coin:
    if c<=k:
        num=k//c
        cnt+=num
        k-=c*num
    if k<=0:
        break

print(cnt)