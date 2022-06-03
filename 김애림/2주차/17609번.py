# 실버 1
# 회문
# 시간초과 해결
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    word = sys.stdin.readline().strip()
    left = list(word)
    right = list(word[::-1])
    if left == right:
        print(0)
    else:
        for i in range(len(word)):
            if left[i] != right[i]:
                del left[i]
                del right[i]
                break
        if left == left[::-1] or right == right[::-1]:
            print(1)
        else:
            print(2)
