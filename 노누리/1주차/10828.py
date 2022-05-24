# input()으로 입력을 받았더니 입력 개수가 많아져서 시간초과가 발생한 문제
# sys.stdin.readline()으로 받아서 시간초과를 없애고
# 주피터로 돌리니까 너무 빨라서 입력을 받지도 않고 돌아가서 겨우 성공한 풀이

import sys
n=int(input())
stack=[]

def empty(stack):
    if len(stack)==0:
        return 1
    else:
        return 0

for _ in range(n):
    command=sys.stdin.readline().split()
    if len(command)==2:
        stack.append(int(command[1]))
    else:
        if command[0]=='pop':
            if empty(stack)==1:
                print('-1')
            else:
                print(stack.pop())
        elif command[0]=='size':
            print(len(stack))
        elif command[0]=='empty':
            print(empty(stack))
        elif command[0]=='top':
            if empty(stack)==1:
                print('-1')
            else:
                print(stack[-1])
