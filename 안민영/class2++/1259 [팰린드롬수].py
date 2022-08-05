import sys

input = sys.stdin.readline

while True :
    word = input().strip()
    if word == '0' : break

    re_word = word[::-1]
    if word == re_word :
        print('yes')
    else : print('no')
