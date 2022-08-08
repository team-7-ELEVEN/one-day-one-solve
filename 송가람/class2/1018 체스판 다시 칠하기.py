M, N = map(int,input().split())
input_chess = []
chess1 = ["BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB"]
chess2 = ["WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW"]
cnt1 = 0
cnt2 = 0
cnt_box = []

for i in range(M):
    input_chess.append(input())

for i in range(M - 7):
    for j in range(N - 7):
        for k in range(8):
            for l in range(8):
                if input_chess[i + k][j + l] != chess1[k][l]:
                    cnt1 += 1

                if input_chess[i + k][j + l] != chess2[k][l]:
                    cnt2 += 1

        cnt_box.append(cnt1)
        cnt_box.append(cnt2)
        cnt1 = 0
        cnt2 = 0

print(min(cnt_box))

