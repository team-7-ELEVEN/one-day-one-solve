up, down, H = map(int, input().split())

if (H - up) < (up - down):
    day = 1
else:
    day = (H - up) // (up - down) 
print(day + 1)