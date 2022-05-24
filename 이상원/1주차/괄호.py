'''
https://www.acmicpc.net/problem/9012


6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(

'''


def check(string: str):
    arr = []
    step = len(string)//2
    for item in range(step):
        string = string.replace('()', '')
    string = string.rstrip()
    if len(string) == 0:
        print('YES')
    else:
        print('NO')


n = int(input())
for item in range(n):
    is_vps = input()
    if len(is_vps) % 2 == 1:
        print('NO')
    else:
        check(is_vps)
