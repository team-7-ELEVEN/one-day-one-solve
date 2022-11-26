from datetime import datetime,timedelta
import copy

# datetime쓰지말자!
# def solution(s, times):
#     answer = []
#     today = list(map(int, s.split(':')))
#     time_list = [list(map(int, i.split(':'))) for i in times]
    
#     date_today = datetime.strptime(s, "%Y:%m:%d:%H:%M:%S")

#     def convert_str(list):
#         n_list = list.copy()
#         result = ""
#         for i in range(len(n_list)):
#             n_list[i] = str(n_list[i])
#             if len(n_list[i]) == 1:
#                 result += "0" + n_list[i] + ":"
#             elif i + 1 == len(n_list):
#                 result += n_list[i]
#             else:
#                 result += (n_list[i] + ":") 
#         return result

#     flag = False
#     nxt_day = today.copy()
#     for time in time_list:
#         for i in range(-1, -5, -1):
#             nxt_day[i] = nxt_day[i] + time[i]
#         result = convert_str(nxt_day)
#         print(nxt_day)
#         date_nxtday = datetime.strptime(result, "%Y:%m:%d:%H:%M:%S")
#         if (date_nxtday - date_today).days > 1:
#             flag = True
#         date_today = date_nxtday
    
#     t = datetime.strptime(s, "%Y:%m:%d:%H:%M:%S")
#     d = date_today - t 
#     day = d.days + 1
#     if flag:
#         return [0, day]
#     else:
#         return [1, day]
     


# print(solution(


# "2021:04:12:16:08:35", ["01:06:30:00", "01:04:12:00"]


# ))