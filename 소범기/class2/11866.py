from collections import deque

N,K = list(map(int,input().split()))
data = [ i for i in range(1,N+1)]
dq= deque(data)

result = []
while dq:
    for _ in range(K):
        temp = dq.popleft()
        dq.append(temp)
    temp = dq.pop()
    result.append(temp)

print("<"+str(result)[1:-1]+">")