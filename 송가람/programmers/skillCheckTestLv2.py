#시간초과 ㅎㅎ
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)

# n = int(input())

# def factorial(n):
#     if n > 1:
#         return n * factorial(n-1)
#     else:
#         return 1

# one = 0
# two = n // 2
# if n % 2 != 0: one = 1

# taile = []
# while two >= 0:
#     taile.append(int((factorial(two + one)) / (factorial(two) * factorial(one))))
#     two -= 1
#     one += 2

# taile_num = sum(taile)
# print(taile_num % 1000000007)

def solution(n):
    taile = [0] * 60001
    taile[1] = 1
    taile[2] = 2
    for i in range(3, n + 1):
        taile[i] = (taile[i - 1] + taile[i - 2]) % 1000000007
    return taile[n]


    