num = int(input())

for i in range(1, num + 1) :
    if i == num : print(0)

    nums = list(map(int, str(i)))
    result = sum(nums) + i

    if result == num :
        print(i)
        break

'''
acc = 1

while acc < num :
    temp = str(acc)
    result = acc

    for s in temp : 
        result += int(s)
    if result == num : 
        print(acc)
        break
    acc += 1

if acc == num : print(0)
'''