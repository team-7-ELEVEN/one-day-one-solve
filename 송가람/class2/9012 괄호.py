t = int(input())

for _ in range(t):
    stack = []
    result = True
    for i in input():

        if i == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                result = False
                break
    
    if stack:
        result = False
    
    print( "YES" if result else "NO" )
