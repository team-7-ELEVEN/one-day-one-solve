n = int(input())

waiting = list(map(int, input().split()))

waiting.sort()

time = []
for i in range(1, n+1):
    time.append(sum(waiting[:i]))

print(sum(time))