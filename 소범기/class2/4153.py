while True:
    data = list(map(int,input().split()))
    data.sort()
    a , b , c = data[0],data[1],data[2]
    if a==0 and b==0 and c==0:
        break

    if a==0:
        print("wrong")
    elif a**2+b**2 == c**2:
        print("right")
    else:
        print("wrong")