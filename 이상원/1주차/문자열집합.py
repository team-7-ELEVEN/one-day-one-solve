'''
https://www.acmicpc.net/problem/14425

5 11
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
codeplus
codeminus
startlink
starlink
sundaycoding
codingsh
codinghs
sondaycoding
startrink
icerink


'''
import sys
inputs = sys.stdin.readline

N, M = map(int, inputs().split())
s = set([inputs() for _ in range(N)])
cnt = 0
for _ in range(M):
    t = inputs()
    if t in s:
        cnt += 1
print(cnt)
