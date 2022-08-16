N = int(input())

max_5 = N // 5

while True:

    remain = N-max_5*5

    if remain % 3 == 0:
        result = max_5+remain//3
        break

    if max_5 == 0 and remain%3 != 0:
        result = -1
        break
    # else:
    #     result = N//3
    #     break

    max_5 -=1

print(result)