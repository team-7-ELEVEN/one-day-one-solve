def solution(bakery_schedule, current_time, k):
    answer = -2
    curr_h, curr_m = current_time.split(':')
    schedule = [list(s.split()) for s in (bakery_schedule)]
    for t in schedule:
        h, m = t[0].split(':')

        if int(h) >= int(curr_h):

            if int(h) == int(curr_h) and int(m) < int(curr_m):
                continue
            
            k -= int(t[1])
        if k <= 0:
            ans = ((int(h) - int(curr_h)) * 60) + (int(m) - int(curr_m))
            return ans
        

    return -1

print(solution(

["12:00 10"], "12:00", 11))
#  ["09:05 10", "12:20 5", "13:25 6", "14:24 5"], "12:05", 10