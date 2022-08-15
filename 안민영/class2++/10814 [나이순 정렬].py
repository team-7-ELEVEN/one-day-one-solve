import sys
input = sys.stdin.readline

n = int(input())

member = []
for _ in range(n) :
    age, name = input().split()
    member.append((int(age), name))

member.sort(key = lambda x : x[0])

for m in member :
    print(m[0], m[1]) 