def solution(n, m):
    answer = []
    for i in range(m+1,0,-1):
        if n%i == 0 and m%i == 0:
            answer.append(i)
            break
    for j in range(1, n*m+1):
        if j%n == 0 and j%m == 0:
            answer.append(j)
            break
    return answer

N, M = map(int, input().split())
n = solution(N, M)

for i in range(2):
    print(n[i])