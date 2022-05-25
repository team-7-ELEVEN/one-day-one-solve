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
    idx = 0

    for item in range(len(arr)):
        max_val = max(arr, key=lambda x: x[0])
        max_val = max_val[0]
        if max_val != arr[0][0]:
            pop_val = arr.pop(0)
            arr.append(pop_val)
            item += 1
        elif max_val == arr[0][0]:
            if arr[1] == m:
                break
            else:
                arr.pop(0)
                answer += 1

    return answer + 1


if __name__ == '__main__':
    inputs = sys.stdin.readline
    test_case = int(inputs())

    for test in range(test_case):
        n, m = map(int, inputs().split())
        score = list(map(int, inputs().split()))
        if n == 1:
            print(1)
        else:
            print(print_docs(n, m, score))
