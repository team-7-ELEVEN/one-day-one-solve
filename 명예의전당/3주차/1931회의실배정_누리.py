
n = int(input())
cnt = 0
task = []

for _ in range(n):
    start, end = map(int, input().split())
    task.append((start, end))

task = sorted(task, key=lambda x: (x[1], x[0]))

for i in task:
    print(i)


time = 0

for t in task:
    if t[0] >= time:
        cnt += 1
        time = t[1]

print(cnt)

(1, 4)
(3, 5)
(0, 6)
(5, 7)
(3, 8)
(5, 9)
(6, 10)
(8, 11)
(8, 12)
(2, 13)
(12, 14)
