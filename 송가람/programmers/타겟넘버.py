def solution(numbers, target):
    n_target = (sum(numbers) - target)//2
    
    def comb(target, idx, cnt):
        for i in range(idx, len(numbers)):
            curr = target
            curr -= numbers[i]
            if curr == 0:
                cnt += 1
            elif curr < 0:
                continue
            elif curr > 0:
                cnt += comb(curr, i + 1, 0)

        return cnt
    answer = comb(n_target, 0, 0)
     
    return answer