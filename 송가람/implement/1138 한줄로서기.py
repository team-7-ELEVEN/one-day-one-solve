n = int(input())
long = list(map(int, input().split()))
line = [0] * n
for i in range(n):
    people = long[i]
    k = 0
    idx = 0
    while True:
        if k == people:
            if line[idx] == 0:
                line[idx] = i + 1
                break
        if line[idx] == 0:
            k += 1
        idx += 1

        
print(*line)
