def check(H):
    target = 0
    for i in data:
        if i-H < 0:
            continue
        else:
            target += (i-H)

    return target

N,M = list(map(int,input().split()))
data = list(map(int,input().split()))

start = 1
end = max(data)


while start <= end:
    mid = (start+end) // 2
    target = check(mid)
    remain = M - target
    if remain <= 0:
        start = mid+1
    else:
        end = mid-1

print(end)