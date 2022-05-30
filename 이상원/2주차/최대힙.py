'''
https://www.acmicpc.net/problem/11279


13
0
1
2
0
0
3
2
1
0
0
0
0
0


'''
import heapq
import sys


def main():
    heap = []

    inputs = sys.stdin.readline
    n = int(inputs())
    for item in range(n):
        num = int(inputs())
        if num == 0:
            if len(heap) == 0:
                print(0)
            else:
                _, pop_num = heapq.heappop(heap)
                print(pop_num)
        else:
            heapq.heappush(heap, (-num, num))


if __name__ == '__main__':
    main()
