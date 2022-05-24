from sys import stdin

num = int(stdin.readline())
l = []

for _ in range(num) :
    i = stdin.readline().split()

    if i[0] == 'push' :
        l.append(i[1])
    elif i[0] == 'top' :
        if len(l) < 1 : print(-1)
        else : print(l[len(l)-1])
    elif i[0] == 'pop' :
        if len(l) < 1 : print(-1)
        else : print(l.pop())
    elif i[0] == 'size' :
        print(len(l))
    elif i[0] == 'empty' :
        if len(l) < 1 : print(1)
        else : print(0)

