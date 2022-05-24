def checkParan(_list):
    s=[]
    
    if _list[0] == ")":
        return "NO"
    
    for i in _list:
        if i == "(":
            s.append(i)
        else:
            if len(s)==0:
                return "NO"
            s.pop()
        
    if len(s) == 0:
        return "YES"
    else:
        return "NO" 
    
    
N = int(input())
for _ in range(N):
    target = list(input())
    print(checkParan(target))