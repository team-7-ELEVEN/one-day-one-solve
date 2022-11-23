import math
def solution(rooms, target):
    dir = {}
    ans = []
    for i in rooms:
        num, name = i.split("]")
        num = int(num[1:])
        if "," in name:
            name = list(name.split(","))
            for j in name:
                if j in dir:
                    dir[j] = [dir[j], num]
                else:
                    dir[j] = num
        else:
            if name in dir:
                dir[name] = [dir[name], num]
            else:
                dir[name] = num
    max_dis = math.inf
    min_p = []
    over = []

    for p in dir.copy().keys():
        if type(dir[p]) is list:
            ans.append(p)
            continue
        dis = abs(target - dir[p])
        if dis == 0:
            dir.pop(p)
        elif dis <= max_dis:
            min_p.append(p)
            max_dis = dis
        elif dis > max_dis:
            over.append([p, dis])
    
    over.sort(key=lambda x: -x[1])
    for a in over:
        ans.append(a[0])
    min_p.sort(reverse=True)
    for b in min_p:
        ans.append(b)

    
    print(ans[::-1])


r = ["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"]
solution(r, 403)