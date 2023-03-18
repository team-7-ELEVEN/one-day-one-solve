n = int(input())
nums = list(map(int, input().split()))

#increase
cnt = 1
max_c = 1
for i in range(len(nums) - 1):
    if nums[i] <= nums[i + 1]:
        cnt += 1
    else:
        cnt = 1
    if max_c < cnt:
        max_c = cnt

#decrease
cnt = 1
max_d = 1
for j in range(len(nums) - 1):
    if nums[j] >= nums[j + 1]:
        cnt += 1
    else:
        cnt = 1
    if max_d < cnt:
        max_d = cnt

print(max(max_d, max_c))
    



# 자기야 미안..
# arr = []
# cnt = 0
# max_n = 0
# start = 0
# end = 0

# for i in range(len(nums) - 1):
#     if arr:
#         if arr[-1] == 1:
#             if nums[i] < nums[i + 1]:
#                 end = i + 1
#             elif nums[i] > nums[i + 1]:
#                 cnt = (i + 1) - start
#                 start = end
#                 end = i + 1
#                 arr.append(-1)
#         else:
#             if nums[i] > nums[i + 1]:
#                 end = i + 144
#             elif nums[i] < nums[i + 1]:
#                 cnt = (i + 1) - start
#                 start = end
#                 end = i + 1
#                 arr.append(1)

#     else:
#         if nums[i] < nums[i + 1]:
#             arr.append(1)
#             end = i + 1
#         elif nums[i] > nums[i + 1]:
#             arr.append(-1)
#             end = i + 1
            
#     if max_n < cnt:
#         max_n = cnt

# print(max_n)

    
