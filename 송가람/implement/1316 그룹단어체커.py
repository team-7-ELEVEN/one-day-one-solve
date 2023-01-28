n = int(input())

def group_word_checker(word):
    flag = False
    check = []
    pre = word[0]
    for i in word:
        if i in check:
            flag = True
            return flag

        if pre == i:
            continue
        else:
            check.append(pre)
            pre = i
            
    return flag

cnt = 0
for i in range(n):
    word = input()
    if not group_word_checker(word):
        cnt += 1

print(cnt)