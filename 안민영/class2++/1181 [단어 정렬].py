import sys

n = int(input())
words = [sys.stdin.readline().strip() for _ in range(n)]
answer = []

words = list(set(words))
words.sort()
words.sort(key=len)

for word in words :
    print(word)