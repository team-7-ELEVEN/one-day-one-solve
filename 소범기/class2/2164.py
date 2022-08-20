# 2164 카드 뒤집기
from collections import deque

card = []
N = int(input())
for i in range(1,N+1):
    card.append(i)

card = deque(card)
while len(card) > 1:
    card.popleft()
    temp = card.popleft()
    card.append(temp)

print(card[0])