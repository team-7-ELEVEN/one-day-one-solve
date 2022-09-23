def solution(lottos, win_nums):
    score = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    zero = 0
    same = 0
    for i in range(6):
        if lottos[i] == 0:
            zero += 1
            continue
        for j in range(6):
            if lottos[i] == win_nums[j]:
                same += 1
    max_rate = zero + same
    min_rate = same
    return score[max_rate], score[min_rate]