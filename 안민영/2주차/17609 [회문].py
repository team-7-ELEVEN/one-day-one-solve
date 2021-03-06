from sys import stdin

input = stdin.readline

num = int(input())
# 회문이면 0, 유사 회문이면 1, 둘 모두 아니면 2
for _ in range(num):
    st = input().strip()
    front, back = 0, len(st) - 1  # 포인터 앞 뒤로 옴
    check = 0

    for _ in range(len(st)):
        if front >= back:
            break
        if st[front] == st[back]:
            front += 1
            back -= 1
            continue

        # 뒷 문자 제거했는데 같을 때, 나머지로 회문 되는지 확인
        if st[front] == st[back-1]:
            temp = st[front:back]
            if temp[:] == temp[::-1]:
                check = 1
                break
        # 앞 문자 제거했는데 같으면
        if st[front+1] == st[back]:
            temp = st[front+1:back+1]
            if temp[:] == temp[::-1]:
                check = 1
                break

        check = 2
        break

    print(check)
