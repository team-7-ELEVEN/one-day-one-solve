# w = input()
# count = 0
# n = len(w)
# word_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# for j in range(n):
#     for i in word_list:
#         if i in w:
#             w = w.replace(i, '0', 1)
#             n = len(w)
#             print(w)
#             break
            
# count += len(w)
# print(count)

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*') 
print(len(word))