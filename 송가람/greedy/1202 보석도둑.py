# 시간초과!!!!!!!

n, bag = map(int, input().split())
j = []
for i in range(n):
    j.append(list(map(int, input().split())))
j.sort(key=lambda x: (-x[1], x[0]))

bag_w = [int(input()) for _ in range(bag)]
bag_w.sort()
ans = 0
for i in range(bag):
    for l in range(len(j)):
        if bag_w[i] >= j[l][0]:
            ans += j[l][1]
            del j[l]
            break

print(ans)

