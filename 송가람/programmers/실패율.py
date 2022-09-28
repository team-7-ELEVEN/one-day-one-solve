def solution(N, stages):
    dic = {}
    cleared = len(stages)
    for i in range(1, N + 1):
        clearing = stages.count(i)
        if clearing == 0:
            dic[i] = 0
        else :
            dic[i] = clearing / cleared
            cleared -= clearing
    return sorted(dic, key=lambda x:dic[x], reverse=True)