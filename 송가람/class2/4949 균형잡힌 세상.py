import sys
input = sys.stdin.readline

while True:
    letter = input().rstrip()
    stack = []

    result = False
    if letter == ".":
        break

    for i in letter:
        if i == "(" or i == "[":    
            stack.append(i)
        else:
            if i == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    result = True
            elif i == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    result = True

    if result or stack:
        print("no")
    else:
        print("yes")
    

