import sys

input =  sys.stdin.readline

target = int(input())

cnt = 1
number = 1

while number < target:
    number += cnt*6
    cnt+=1
    
print(cnt)
