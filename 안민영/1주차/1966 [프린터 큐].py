from collections import deque
from sys import stdin

num = int(stdin.readline()) 
for i in range(num) :
    n, m = map(int, stdin.readline().split()) # 문서의 개수, 인쇄할거 몇번째 놓여있는지 
    queue = deque(map(int, stdin.readline().split())) # 1 1 9 1 1 1
    cnt = 0
    curr = m

    while queue :
        max_priority = max(queue) # 1

        while queue :
            p = queue.popleft()
            
            if p == max_priority :
                cnt += 1
                m -= 1 
                break
            else :
                queue.append(p)
                m -= 1
                if curr < 0 : curr = len(queue) -1
        
        if curr < 0 :
            print(cnt)
            break

                



