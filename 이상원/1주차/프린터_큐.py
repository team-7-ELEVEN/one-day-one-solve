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
import collections
import sys


def print_docs(n, m, score: list):
    deq = collections.deque()
    for idx, item in enumerate(score):
        deq.append((idx, item))
    answer = 0
    while True:
        max_val = max(deq, key=lambda x: x[1])
        max_val = max_val[1]
        if max_val != deq[0][1]:
            pop_tuple = deq.popleft()
            deq.append(pop_tuple)
        elif max_val == deq[0][1] and m != deq[0][0]:
            deq.popleft()
            answer += 1
        elif max_val == deq[0][1] and m == deq[0][0]:
            answer += 1
            break
    return answer


if __name__ == '__main__':
    inputs = sys.stdin.readline
    test_case = int(inputs())

    for test in range(test_case):
        n, m = map(int, inputs().split())
        score = list(map(int, inputs().split()))
        print(print_docs(n, m, score))
