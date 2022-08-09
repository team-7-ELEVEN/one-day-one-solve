N = int(input())
apo = 666
cnt = 0

while True:
    if str(apo).find("666") != -1:
        cnt += 1

    if cnt == N:
        print(apo)
        break
    
    apo += 1
