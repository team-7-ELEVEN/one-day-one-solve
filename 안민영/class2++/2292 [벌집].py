num = int(input())

# 1 2 8 20 38 ...
#    6 12 24 ... 6n

'''
n = 1
while True :
    if ((3 * n * n) - (3 * n) + 2) <= num :
        n += 1
    else :
        print(n)
        break
'''

k = 1
n = 1
while True :
    if k < num :
        k += n * 6
        n += 1
    else :
        print(n)
        break
