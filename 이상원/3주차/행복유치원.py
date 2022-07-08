'''
https://www.acmicpc.net/problem/13164

n명의 원생을 키 순으로 세고 k개의 조로 나누려고 한다 
각 조에는 최호 한명이 있어야 하고 같은 조에 속한 원생은 서로 인접해야 한다 
조별로 인원수고 같을 필요는 없다 

나눠진 조들은 단체 셔츠를 맞추려고 한다 
티 맞추는 비용은 조에서 가장 키가 큰 원생과 가장 키가 작은 원생의 키 차이만큼 든다 
비용을 아끼고 싶은 태양이는 k개의 조에 대해 티셔츠 만드는 비용의 합을 최소로 하고 싶어 한다 
최소 비용을 구하자 



5 3
1 3 5 6 10


'''


import sys


def solution(n, k, length: list):
    cost = []
    for i in range(n-1):
        cost.append(length[i+1] - length[i])
    cost.sort()
    print(sum(cost[:n-k]))


def main():
    inputs = sys.stdin.readline
    n, k = map(int, inputs().split())
    length = list(map(int, inputs().split()))
    solution(n, k, length)


if __name__ == '__main__':
    main()
