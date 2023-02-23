from collections import Counter

def solution(k, tangerine):
    tanges = Counter(tangerine).most_common()
    ans = 0
    print(tanges)
    for t in tanges:
        if t[1] >= k:
            ans += 1
            return ans
        else:
            k -= t[1]
            ans += 1


print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))