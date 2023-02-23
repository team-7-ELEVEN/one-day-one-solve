# sum을 반복문안에 넣어서 돌리면 시간초과가 난다..
from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    cnt = 0
    s1 = sum(queue1)
    s2 = sum(queue2)
    while True:
        if s1 > s2:
            q = queue1.popleft()
            queue2.append(q)
            s1 -= q
            s2 += q
            cnt += 1
        elif s1 < s2:
            q = queue2.popleft()
            queue1.append(q)
            s2 -= q
            s1 += q
            cnt += 1
        else:
            return cnt
        if cnt == (len(queue1) * 4):
            return -1

print(solution([1, 2, 1, 2], [1, 10, 1, 2]))