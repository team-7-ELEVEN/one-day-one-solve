import sys
input = sys.stdin.readline
stack = []
for _ in range(int(input())):
    command = input().strip()

    if command == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif command == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        stack.append(int(command.split()[-1]))
