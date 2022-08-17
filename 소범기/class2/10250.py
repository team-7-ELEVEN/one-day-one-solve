import sys
input = sys.stdin.readline

def solution(H,W,M):
        # 호수
        # 호수는 몫에 해당된다        
    ho_number = M//H + 1
    
    flow_number = M % H

    if flow_number == 0:
        flow_number = H
        ho_number -= 1

    if ho_number < 10:
        ho_number = "0"+str(ho_number)
    else:
        ho_number = str(ho_number)

    return str(flow_number) + ho_number

N = int(input())


for _ in range(N):
    H,W,M = list(map(int,input().split()))
    print(int(solution(H,W,M)))
