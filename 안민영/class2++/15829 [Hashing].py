import sys
input = sys.stdin.readline

n = int(input())
plain = input()

answer = 0
for i in range(n) :
    answer += (ord(plain[i])-96) * (31**i)

print(int(answer) % 1234567891)