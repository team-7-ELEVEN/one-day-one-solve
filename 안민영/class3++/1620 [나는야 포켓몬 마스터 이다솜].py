'''
# 메모리, 시간 더 걸림
from sys import stdin
input = stdin.readline

n, m = map(int, input().strip().split())
p_dict = dict()
for i in range(1, n+1) :
    x = input().strip()
    p_dict[str(i)] = x
    p_dict[x] = str(i)

for i in range(m) :
    x = input().strip()
    print(p_dict[x])
'''

from sys import stdin
input = stdin.readline

n, m = map(int, input().strip().split())
p_dict = dict()
for i in range(1, n+1) :
    p_dict[i] = input().strip()
p_re_dict = dict(map(reversed, p_dict.items()))

for i in range(m) :
    x = input().strip()
    
    if ord(x[0]) >= ord('A') :
        print(p_re_dict[x])
    else :
        print(p_dict[int(x)])