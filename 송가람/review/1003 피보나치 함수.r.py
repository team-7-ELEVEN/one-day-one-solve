T = int(input())

zero = {0: 1, 1: 0, 2: 1}
one = {0: 0, 1: 1, 2: 1}
for i in range(T):
    N = int(input())
    if N > 2:
        for i in range(3, N + 1):
            zero[i] = zero[i - 1] + zero[i - 2]
            one[i] = one[i - 1] + one[i - 2]
    print(zero[N], one[N])
