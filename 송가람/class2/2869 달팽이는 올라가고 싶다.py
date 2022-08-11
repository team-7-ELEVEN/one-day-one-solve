up, down, H = map(int, input().split())
day = (H - up) // (up - down) + 1
if (H - up) % (up - down):
    day += 1
print(day)