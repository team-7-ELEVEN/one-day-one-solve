from sys import stdin

n, m = map(int, stdin.readline().split())
s_list = [stdin.readline().strip() for _ in range(n)]
str_list = [stdin.readline().strip() for _ in range(m)]
cnt = 0

for str in str_list :
    if str in s_list :
        cnt += 1

print(cnt)