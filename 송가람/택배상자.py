def solution(order):
    answer = 0
    stack = []
    n = len(order)
    cont = 1
    i = 0
    while i < n:
        if order[i] == cont:
            answer += 1
            cont += 1
            i += 1
            continue
        if stack:
            if stack[-1] == order[i]:
                stack.pop()
                answer += 1
                i += 1
                continue
        if order[i] != cont:
            stack.append(cont)
            cont += 1
        if cont > n:
            break

    return answer
