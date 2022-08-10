from sys import stdin
input = stdin.readline

n = int(input())
l = set(input().split())

m = int(input())
x = input().split()

for i in x :
    if i in l :
        print(1)
    else : print(0)

