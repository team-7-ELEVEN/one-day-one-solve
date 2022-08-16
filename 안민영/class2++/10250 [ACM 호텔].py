from sys import stdin
input = stdin.readline

def assign(h, w, n) :
    count = 0
    for i in range(w) :
        for j in range(h) :
            count += 1
            if count == n :
                return (j+1)*100 + (i+1)

t = int(input())
for _ in range(t) : 
    h, w, n = map(int, input().split())

    print(assign(h, w, n))