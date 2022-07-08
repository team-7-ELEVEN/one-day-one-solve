import sys
n = int(input())
office_t = []
for _ in range(n):
    x = list(map(int, sys.stdin.readline().split()))
    office_t.append(x)
office_t.sort()

for i in office_t:
    print(i)


count = 1
while len(office_t) >= 2:
    if office_t[0][1] > office_t[1][0] and office_t[0][1] > office_t[1][1]:
        del office_t[0]
    elif office_t[0][1] <= office_t[1][0]:
        del office_t[0]
        count += 1
    else:
        del office_t[1]
print(count)


# [0, 6]
[1, 4]
# [2, 13]
# [3, 5]
# [3, 8]
[5, 7]
# [5, 9]
# [6, 10]
[8, 11]
# [8, 12]
[12, 14]
