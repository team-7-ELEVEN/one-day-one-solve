from collections import deque
T = int(input())
# N 문서의 갯수
# M 궁금해 하는 문서
# 이때 맨 왼쪽 0번째 라고하자
for _ in range(T):
    N,M = list(map(int,input().split()))
    data = list(map(int,input().split()))
    data_preprocess = []
    for i,v in enumerate(data):
        data_preprocess.append((v,i))

    dq = deque(data_preprocess)

    cnt = 0
    while True:
        prior = max(dq)
    
        while True:
            temp = dq.popleft()
            if temp[0] == prior[0]:
                cnt+=1
                break
            else:
                dq.append(temp)
        
        if temp[1] == M:
            print(cnt)
            break