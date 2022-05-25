'''
https://www.acmicpc.net/problem/1966

3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1

'''
import heapq
import sys


def print_docs(n, m, score: list):
    arr = []
    answer = 0
    for idx, val in enumerate(score):
        arr.append((val, idx))

    while True:
        max_val =


if __name__ == '__main__':
    inputs = sys.stdin.readline
    test_case = int(inputs())

    for test in range(test_case):
        n, m = map(int, inputs().split())
        score = list(map(int, inputs().split()))
        print(print_docs(n, m, score))
