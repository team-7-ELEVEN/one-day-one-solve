def check(data):
    cnt1 = 0
    for i in range(8):
        if i % 2 == 0:
            for j in range(8):
                if j % 2 == 0:
                    if data[i][j] == "W":
                        cnt1+=1
                    else:
                        continue
                else:
                    if data[i][j] == "B":
                        cnt1+=1
                    else:
                        continue
        else:
            for j in range(8):
                if j % 2 == 0:
                    if data[i][j] == "B":
                        cnt1+=1
                    else:
                        continue
                else:
                    if data[i][j] == "W":
                        cnt1+=1
                    else:
                        continue
    cnt2 = 0
    for i in range(8):
        if i % 2 == 0:
            for j in range(8):
                if j % 2 == 0:
                    if data[i][j] == "B":
                        cnt2+=1
                    else:
                        continue
                else:
                    if data[i][j] == "W":
                        cnt2+=1
                    else:
                        continue
        else:
            for j in range(8):
                if j % 2 == 0:
                    if data[i][j] == "W":
                        cnt2+=1
                    else:
                        continue
                else:
                    if data[i][j] == "B":
                        cnt2+=1
                    else:
                        continue
    return min(cnt1,cnt2)

import sys

input = sys.stdin.readline

N,M= list(map(int,input().split()))
data = []
for _ in range(N):
    input_data = input().rstrip()
    data.append(input_data)
    
min_value= float("inf")
for i in range(N-7):
    for j in range(M-7):
        mat = []
        for x in range(8):
            mat.append(data[i+x][j:j+8])
        isgood = check(mat)
        min_value = min(min_value,isgood) 
print(min_value)