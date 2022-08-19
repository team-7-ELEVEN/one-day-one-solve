import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    rank = []
    for _ in range(n):
        rank.append(list(map (int, input().split())))

    rank.sort()
    min_rank = rank[0][1]
    cnt = 1

    for i in range(1, n):
        if min_rank > rank[i][1]:
            min_rank = rank[i][1]
            cnt += 1
    print(cnt)

# 완전탐색 시간초과
# for _ in range(int(input())):
#     n = int(input())
#     rank = []
#     ans = []
#     for _ in range(n):
#         rank.append(list(map (int, input().split())))

#     for i in range(n):
#         for j in range(n):
#             if rank[i][0] > rank[j][0] and rank[i][1] > rank[j][1]:
#                 ans.append(i)
#                 break
#     print(n - len(ans))