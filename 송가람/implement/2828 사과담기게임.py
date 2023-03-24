from collections import deque
n, m = map(int, input().split())
apple = [int(input()) for _ in range(int(input()))]
basket = deque(list(range(1, m + 1)))

cnt = 0
for a in apple:
    while True:
        if a in basket:
            break
        else:
            if a > max(basket):
                basket.append(basket[-1] + 1)
                basket.popleft()
                cnt += 1
            elif a < min(basket):
                basket.appendleft(basket[0] - 1)
                basket.pop()
                cnt += 1

print(cnt)