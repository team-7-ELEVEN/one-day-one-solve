num = int(input())
count = 0
check = 0

while True :
    count += 1
    if '666' in str(count) :
        check += 1
        if num == check :
            print(count)
            break

# while True :
#     count += 1
#     if str(count).find('666') >= 0 :
#         check += 1
#         if num == check :
#             print(count)
#             break
