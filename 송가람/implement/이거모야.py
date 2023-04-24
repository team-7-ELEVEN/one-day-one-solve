import random

# 숫자 -> 영어
string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = [i for i in range(26)]

dict_ = {}
for a,b in zip(string,number):
    dict_[b+1] = a
    


print("숫자에서 영어로")
x = int(input("몇문제 풀래??  "))

problem = []
your_sol = []
wrong_list = []
for _ in range(x):
    a = random.randint(1,26)
    print(a)
    q = input("대문자로 적어주세요 : ")
    if dict_[a] == q:
        print("정답입니다.")
    else:
        print("똑바로 정신 차리세요")
        wrong_list.append((a,q))
    
print("오답리스트")
print(wrong_list)