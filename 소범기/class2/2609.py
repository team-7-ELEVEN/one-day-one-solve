def uclidian(M,N):
    if M<N:
        M,N = N,M

    if M % N == 0:
        return N
    else:
        return uclidian(N,M%N)
        
M,N = list(map(int,input().split()))
GCD = uclidian(M,N)
print(GCD)
print(M*N//GCD)
