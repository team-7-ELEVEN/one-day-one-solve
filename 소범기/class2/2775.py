N = int(input())

for _ in range(N):
    # K층
    K = int(input())
    # N호
    N = int(input())
    # 0층 사람
    inital_floor = [ x for x in range(1,N+1)]

    for _ in range(K):
        upfloor = []
        for i in range(1,N+1):
            upfloor.append(sum(inital_floor[:i]))
        inital_floor=upfloor
    print(inital_floor[N-1])