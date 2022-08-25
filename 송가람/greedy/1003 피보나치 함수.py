t = int(input())
zero = [1, 0, 1]
one = [0, 1, 1]


def fibo(n):
    length = len(zero)
    for i in range(length, n + 1):
        zero.append(zero[i - 1] + zero[i - 2])
        one.append(one[i - 1] + one[i - 2])
    return zero[n], one[n]

for _ in range(t):
    n = int(input())
    print(*fibo(n))
    