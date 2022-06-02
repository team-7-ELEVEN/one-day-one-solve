'''
https://www.acmicpc.net/problem/17609

7
abba
summuus
xabba
xabbay
comcom
comwwmoc
comwwtmoc


'''


import sys


def ispseudo(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def palindrome(word, left, right):
    if word == word[::-1]:
        return 0
    else:
        while left < right:
            if word[left] != word[right]:
                check_left = ispseudo(word, left + 1, right)
                check_right = ispseudo(word, left, right - 1)

                if check_left or check_right:
                    return 1
                else:
                    return 2
            else:
                left += 1
                right -= 1


def main():
    inputs = sys.stdin.readline
    n = int(inputs())
    for _ in range(n):
        word = inputs().rstrip('\n')
        left, right = 0, len(word)
        palindrome(word, left, right)


if __name__ == '__main__':
    main()
