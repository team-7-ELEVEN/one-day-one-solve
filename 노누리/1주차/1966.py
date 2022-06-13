# 한번에 성공!

def printer_queue(queue,m):
    cnt=1
    while queue:
        num=queue.pop(0)
        for i in range(len(queue)):
            if num[0]<queue[i][0]:
                queue.append(num)
                break
            else:
                if i==len(queue)-1:
                    if num[1]==m:
                        return cnt
                    else:
                        cnt+=1
    return cnt

T=int(input())
for _ in range(T):
    n,m=map(int,input().split())
    input_queue=list(map(int,input().split()))
    queue=[(input_queue[i],i) for i in range(len(input_queue))]
    print(printer_queue(queue,m))
