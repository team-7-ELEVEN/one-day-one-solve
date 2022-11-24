def solution(cards):
    answer = []
    opened = []

    def get_box_num(idx):
        new_open = 0
        while True:
            i = cards[idx]
            if i in opened:
                break
            else:
                opened.append(i)
                new_open += 1
                idx = i - 1   
        return new_open

    for j in range(len(cards)):
        if not (cards[j] in opened):
            box_num = get_box_num(j)
            answer.append(box_num)

    answer.sort(reverse=True)
    if len(answer) == 1:
        return(0)
    else:
        return(answer[0] * answer[1])


print(solution([8,6,3,7,2,5,1,4]))