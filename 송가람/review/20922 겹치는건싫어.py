# N, K = map(int, input().split())
# nums = list(map(int, input().split()))

# dic = {}
# end = 0
# for start in range(N):
#     if nums[end] not in dic:
#         dic[nums[end]] = 1

#     if dic[nums[end]] > K:
#         dic[nums[start]] -= 1

#     while dic[nums[end]] <= K and end < N:
#         if nums[end] not in dic:
#             dic[nums[end]] = 1
#         else:
#             dic[nums[end]] += 1

#         end += 1

# 겹치는 건 싫어!
import sys

rl = sys.stdin.readline


def solve(N, K, array):
    cnt = dict()
    max_length = 1
    start = 0
    end = 0
    flag = False
    while start <= end and end < N:
        if start + max_length > N:
            flag = True
            break
    
        elif array[end] not in cnt:
            cnt[array[end]] = 1
            end += 1

        elif cnt[array[end]] <= K:
            cnt[array[end]] += 1
            
            while cnt[array[end]] > K:
                max_length = end - start if max_length < end - start else max_length
                cnt[array[start]] -= 1
                start += 1
                
            end += 1

    if not flag and end - start > max_length:
        max_length = end - start
    print(max_length)
    return


if __name__ == '__main__':
    N, K = map(int, rl().split())
    array = list(map(int, rl().split()))
    solve(N, K, array)
