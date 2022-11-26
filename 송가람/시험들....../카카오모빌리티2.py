def solution(id_list, k):
    dic = {}
    for i in id_list:
        ids = list(set(i.split()))
        for id in ids:
            if not (id in dic):
                dic[id] = 1
            elif id in dic:
                dic[id] += 1
            
            if dic[id] >= k:
                dic[id] = k
                continue
               
    return sum(dic[item] for item in dic)

print(solution(
["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"], 3
))

