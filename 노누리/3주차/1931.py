# n=int(input())
# cnt=0
# task=[]
# time=[]

# for _ in range(n):
#     start,end=map(int,input().split())
#     task.append((start,end))

# task=sorted(task,key=lambda x:(x[1]-x[0]))

# for t in task:
#     if t[0] not in time and t[1] not in time:
#         cnt+=1
#         for i in range(t[0],t[1]+1):
#             time.append(i)

# print(cnt)

# 위에 코드는 시간초과!

n=int(input())
cnt=0
task=[]

for _ in range(n):
    start,end=map(int,input().split())
    task.append((start,end))

task=sorted(task,key=lambda x:(x[1],x[0]))
time=0

for t in task:
    if t[0]>=time:
        cnt+=1
        time=t[1]

print(cnt)
