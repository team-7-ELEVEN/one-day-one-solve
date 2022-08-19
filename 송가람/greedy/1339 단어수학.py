import sys
input = sys.stdin.readline
n = int(input())
dic = {}

for _ in range(n):
    word = input().rstrip()
    for i in range(len(word)):
        if word[i] in dic:
            dic[word[i]] += 10 ** (len(word) - i - 1)
        else:
            dic[word[i]] = 10 ** (len(word) - i - 1)

sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
ans = 0
num = 9

for i in range(len(sorted_dic)):
    ans += sorted_dic[i][1] * num
    num -= 1
print(ans)



# a = {}
# ipt = "abba"
# idx = 0
# for i in ipt:
#     if i in a:
#         a[i] += 10 ** (len(ipt) - idx - 1)
#     else:
#         a[i] = 10 ** (len(ipt) - idx - 1)
#         idx += 1
# print(a)
