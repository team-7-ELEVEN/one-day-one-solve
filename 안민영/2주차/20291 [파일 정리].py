from sys import stdin
input = stdin.readline

num = int(input())
ext = {}

for _ in range(num) :
    file = input()
    index = file.find(".")
    e = file[index+1:].strip()

    # defaultdict(int) 사용해보기
    if e in ext :
        ext[e] += 1
    else : ext[e] = 1

for (key, value) in sorted(ext.items()) :
    print(key, value)