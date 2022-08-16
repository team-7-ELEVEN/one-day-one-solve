import sys
input = sys.stdin.readline

N = int(input())

data=[]

for _ in range(N):
    data.append(int(input()))

sort_data = sorted(data)
# N은
# 산술평균 
ari_mean = sum(sort_data)/N

print(round(ari_mean))

median = sort_data[(N+1)//2-1]
print(median)

from collections import Counter
a = Counter(sort_data).most_common()

if len(a) == 1:
    print(a[0][0])
elif a[0][1] == a[1][1]:
    print(a[1][0])
else:
    print(a[0][0])


print(sort_data[-1]-sort_data[0])