def solution(flowers):
    answer = 0
    dic = {}
    for s, e in flowers:
        for j in range(s, e):
            if not (j in dic):
                dic[j] = True

    return len(dic)


print(solution(
[[3, 4], [4, 5], [6, 7], [8, 10]]))