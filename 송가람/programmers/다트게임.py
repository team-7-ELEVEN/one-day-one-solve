def solution(dartResult):
    answer = []
    score = ""
    for i in dartResult:
        if i.isnumeric():
            score += i
        elif i == "S":
            score = int(score) ** 1
            answer.append(score)
            score = ""
        elif i == "D":
            score = int(score) ** 2
            answer.append(score)
            score = ""
        elif i == "T":
            score = int(score) ** 3
            answer.append(score)
            score = ""
        elif i == "*":
            if len(answer) <= 1:
                answer[-1] *= 2
            else:
                answer[-1] *= 2
                answer[-2] *= 2
        elif i == "#":
            answer[-1] = -answer[-1]
    return sum(answer)