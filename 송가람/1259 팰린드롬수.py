while True:
    int_palin = int(input())
    str_palin = str(int_palin)
    check = 0
    if 0 == int_palin:
        break

    for i in range(int(len(str_palin) / 2)):
        if str_palin[i] != str_palin[-(i+1)]:
            check += 1
    
    if check > 0:
        print("no")
    else:
        print("yes")

        
