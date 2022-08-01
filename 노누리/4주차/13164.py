n,k=map(int,input().split())
height=list(map(int,input().split()))
answer=[]

for i in range(n-1):
    answer.append(height[i+1]-height[i])

answer.sort()

print(sum(answer[:n-k]))
