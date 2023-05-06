def solution():
    n, t, p = map(int, input().split())
    if not n: return 1 if p else -1
    score = list(map(int, input().split()))
    full = False
    a = 1
    if n == p:
        full = True
    for i in range(len(score)):
        if score[i] < t:
            return a
        elif score[i] == t:
            if full:
                if score[-1] < t:
                    return a
                else:
                    return -1
            else:
                return a
        a += 1
    if full:
        return -1
    else:
        return a

print(solution())