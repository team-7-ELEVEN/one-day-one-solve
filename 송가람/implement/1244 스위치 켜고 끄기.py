N = int(input())
switch = list(map(int, input().split()))

def switch_female(idx):
    before = idx - 1
    after = idx + 1
    while True:
        if 0 <= before and after < N:
            if switch[before] == switch[after]:
                switch[before] = int(bin(not switch[before])[2:])
                switch[after] =  int(bin(not switch[after])[2:])
                before -= 1
                after += 1
            else:
                return
        else:
            return

def switch_male(idx):
    n = 1
    while True:
        if idx * n <= N:
            switch[(idx * n) - 1] = int(bin(not switch[(idx * n) - 1])[2:])
            n += 1
        else:
            return
            

for _ in range(int(input())):
    gender, n = map(int, input().split())
    if gender == 1:
        switch_male(n)
    else:
        switch[n - 1] = int(bin(not switch[n - 1])[2:])
        switch_female(n - 1)

for i in range(N):
    if i != 0 and i % 20 == 0:
        print()
    print(switch[i], end=' ')
print()

