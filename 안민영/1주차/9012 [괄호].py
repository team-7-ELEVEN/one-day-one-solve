from sys import stdin

num = int(stdin.readline())
ps = [list(stdin.readline().strip()) for _ in range(num)]

def solution(ps) :
    check = []
    for s in ps :
        if s == '(' :
            check.append('(')
        else : 
            if len(check) > 0 :
                check.pop()
            else : 
                return 'NO'
    if len(check) < 1 :
        return 'YES'
    else : return 'NO'


for l in ps :
    print(solution(l))