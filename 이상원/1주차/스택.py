'''
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
'''
from inspect import stack
import sys


def push(val, lst: list):
    lst.append(val)
    return lst


def top(lst: list):
    if lst:
        print(lst[-1])
    else:
        print(-1)


def pop(lst: list):
    if not lst:
        print(-1)
    else:
        print(lst[-1])
        return lst[:-1]


def size(lst: list):
    if not lst:
        print(0)
    else:
        print(len(lst))


def empty(lst: list):
    if not lst:
        print(1)
    else:
        print(0)


inputs = sys.stdin.readline
n = int(inputs())

stack_lst = []
for item in range(n):
    if not stack_lst:
        stack_lst = []
    command = inputs().split()
    if command[0] == 'push':
        stack_lst = push(command[1], stack_lst)
    elif command[0] == 'pop':
        stack_lst = pop(stack_lst)
    elif command[0] == 'size':
        size(stack_lst)
    elif command[0] == 'empty':
        empty(stack_lst)
    elif command[0] == 'top':
        top(stack_lst)
