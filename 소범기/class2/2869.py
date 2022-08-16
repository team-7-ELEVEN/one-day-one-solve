A,B,V = list(map(int,input().split()))
# days = 0
# climing = 0

# while True:
#     climing += A
#     days+=1
#     if climing >= V:
#         print(days)
#         break
#     else:
#         climing-=B

# 1000 1 1002
# 하루에 올라가는 거리
oneday= A-B

days = (V-A)//oneday
# 이나머지가 있을경우 몫+1
# v-a/a-b 
if (V-A)%oneday != 0:
    print(days+2)
else:
    print(days+1)