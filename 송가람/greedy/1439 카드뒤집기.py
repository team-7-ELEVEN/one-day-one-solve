card = input()
mem = card[0]
cnt = 1
for i in card:
    if mem != i:
        cnt += 1
        mem = i

print(int(cnt / 2))