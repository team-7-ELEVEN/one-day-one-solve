def factorial(N):
    if N == 0:
        return 1
    return N*factorial(N-1)

N,K = list(map(int,input().split()))

result = factorial(N)/(factorial(K)*factorial(N-K))
print(int(result))