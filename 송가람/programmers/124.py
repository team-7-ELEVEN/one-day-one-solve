## 시간초과!
# def solution(n):
#     nums = ["1", "2", "4"]
#     N = 0
#     cnt = 3
#     if n <= 3:
#         return nums[n - 1]
    
#     while True:
#         for i in range(N, N+3):
#             for j in ["1", "2", "4"]:
#                 nums.append(nums[i] + j)
#                 cnt += 1
#                 if n == cnt:
#                     return nums[n - 1]
#                     break
#         N += 3

# print(solution(13))


# def solution(n):

#     r = n % 3
#     q = n // 3

#     return 

## 지운님이 다햇음!
def something(n):
	if n%3 == 0:
		return(n//3 - 1, 4)
	else:
		return(n//3, n%3)

def solution(target):
    s = []
    while target>0:
        target, a = something(target)
        s.append(a)
    s.reverse()
    s = list(map(str, s))
    s = "".join(s)
    return s
