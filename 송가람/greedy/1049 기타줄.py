n, brand = map(int, input().split())
box, single = [], []
for _ in range(brand):
    b, s = map(int, input().split())
    box.append(b)
    single.append(s)

if min(box) < min(single) * (n % 6):
    print(min(box) * (n // 6 + 1))
elif (min(box) * (n // 6)) > min(single) * n:
    print(min(single) * n)
else:
    print((min(box) * (n // 6)) + (min(single) * (n % 6)))


