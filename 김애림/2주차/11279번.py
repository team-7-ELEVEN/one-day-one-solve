# 최대 힙
n = int(input())
result = []
for _ in range(n):
    x = int(input())
    if x > 0:
        result.append(x)
    else:
        if result:
            print(max(result))
            result.remove(max(result))
        else:
            print(0)
