# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초 (하단 참고)	1536 MB	11163	6134	4326	55.697%

# 문제
# 총 N개의 문자열로 이루어진 집합 S가 주어진다.

# 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다.

# 다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.

# 다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.

# 입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다. 집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.

# 출력
# 첫째 줄에 M개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지 출력한다.
'''
5 11
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
codeplus
codeminus
startlink
starlink
sundaycoding
codingsh
codinghs
sondaycoding
startrink
icerink

4
'''


if __name__=="__main__":
    N,M = list(map(int,input().split()))
    # N개의 입력값 string을 list에 추가한다.
    check_list = []
    for _ in range(N):
        list_val = input()
        check_list.append(list_val)
        
    check_value = []
    for _ in range(M):
        checking = input()
        check_value.append(checking)
    
    count = 0
    
    for i in range(M):
        if check_value[i] in check_list:
            count+=1

print(count)