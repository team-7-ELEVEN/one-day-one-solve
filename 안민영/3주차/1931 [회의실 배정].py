import sys
input = sys.stdin.readline

n = int(input())
time_table = [list(map(int, input().split())) for _ in range(n)]
time_table.sort(key = lambda x : (x[1], x[0])) # 끝나는 시간 우선순위 정렬
cnt, prev_end = 0, 0

# 다음 회의 시작 시간이 이전 회의 끝나는 시간보다 늦게 시작한다면 cnt++
for start, end in time_table :
    if prev_end <= start :
        cnt += 1
        prev_end = end

print(cnt)