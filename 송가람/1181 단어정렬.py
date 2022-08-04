n = int(input())
word_list = []
sort_list = []

for i in range(n):
    word_list.append(input())

word_list = list(set(word_list))

for i in word_list:
    sort_list.append((len(i), i))

sort_list.sort()

for word_len, word in sort_list:
    print(word)