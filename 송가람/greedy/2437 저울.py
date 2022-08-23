n = int(input())
choo = list(map(int, input().split()))  
choo.sort()
target = 1

for i in choo:
    if target >= i:
        target += i
    else:
        break

print(target)
# n = int(input())
# choo = list(map(int, input().split()))  
# choo.sort(reverse=True)
# find = False

# for i in range(1, sum(choo) + 1):
#     check = i
#     while True:
#         for j in choo:
#             if i >= j:
#                 i -= j
#         if i == 0:
#             break
#         else:
#             find = True
#             break
#     if find:
#         print(check)
#         break