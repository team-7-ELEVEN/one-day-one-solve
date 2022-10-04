def solution(today, terms, privacies):
    ans = []
    term = {}
    today = list(map(int, today.split(".")))
  
    for i in terms:
        t, d = i.split(" ")
        term[t] = int(d)

    for j in range(len(privacies)):
        date, T = privacies[j].split(" ")
        due_date = list(map(int, date.split(".")))
        month = due_date[1] + term[T]
        if month <= 12:
            due_date[1] = month
            due_date[2] -= 1
            if due_date[2] == 0:
                due_date[1] -= 1
                due_date[2] = 28
            
            for i in range(3):
                if today[i] < due_date[i]:
                    break
                elif today[i] > due_date[i]:
                    ans.append(j + 1)
                    break
        else:
            rest = month % 12 
            year = month // 12
            due_date[0] += year
            due_date[1] = rest
            due_date[2] -= 1
            if due_date[2] == 0 and due_date[1] == 0:
                due_date[2] = 28
                due_date[1] = 12
                due_date[0] -= 1
            if due_date[2] == 0:
                due_date[1] -= 1
                due_date[2] = 28
            if due_date[1] == 0:
                due_date[1] = 12
                due_date[0] -= 1
            for i in range(3):
                if today[i] < due_date[i]:
                    break
                elif today[i] > due_date[i]:
                    ans.append(j + 1)
                    break

    return ans


print(solution(
"2020.01.01", ["Z 2", "D 5"], ["2019.01.01 Z", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))