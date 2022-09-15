import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_list = set(input().strip() for _ in range(n))
m_list = set(input().strip() for _ in range(m))

result = sorted(list(n_list&m_list))
print(len(result))
for x in result :
    print(x)