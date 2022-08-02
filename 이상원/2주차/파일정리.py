'''
https://www.acmicpc.net/problem/20291


8
sbrus.txt
spc.spc
acm.icpc
korea.icpc
sample.txt
hello.world
sogang.spc
example.txt


'''
import collections
import operator
import sys


def main():
    def_dict = collections.defaultdict(int)
    inputs = sys.stdin.readline
    n = int(inputs())
    for item in range(n):
        fileName = str(inputs())
        name, hwak = fileName.split('.')
        def_dict[hwak[:-1]] += 1

    def_dict = sorted(def_dict.items(), key=operator.itemgetter(0))

    for val, num in def_dict:
        print(f'{val} {num}')


if __name__ == '__main__':
    main()
