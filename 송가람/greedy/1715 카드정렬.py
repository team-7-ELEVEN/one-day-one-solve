import sys
input = sys.stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]
comb = 0
while len(cards) > 1:
    cards.sort()
    cards[0] = cards[0] + cards[1]
    comb += cards[0]
    cards.pop(1)
 
print(comb)
