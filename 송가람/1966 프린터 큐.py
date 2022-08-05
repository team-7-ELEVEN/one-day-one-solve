from collections import deque
n = int(input())

def printer_queue():
    N, M = map(int, input().split())
    dq = deque(list(map(int, input().split())))
    cnt = 0
    if N == 1:
        return 1
    else:
        for i in range(N):
            dq[i] = (dq[i], i)

        while True:
            if dq[0][0] == max(dq)[0]:
                cnt += 1
                if dq[0][1] == M:
                    return cnt
                    break
                else:
                    dq.popleft()
            else:
                dq.append(dq.popleft())


for _ in range(n):
    print(printer_queue())

