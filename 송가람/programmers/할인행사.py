import copy
def solution(want, number, discount):
    dic = {}
    for type, n in zip(want, number):
        dic[type] = n
    ans = 0
    
    start_day = 0
    while start_day + 10 <= len(discount):
        cpy_dic = dic.copy()
        end_day = start_day + 10
        for i in range(start_day, end_day):
            if discount[i] in cpy_dic:
                cpy_dic[discount[i]] -= 1
                if cpy_dic[discount[i]] == 0:
                    cpy_dic.pop(discount[i])

            if not cpy_dic:
                ans += 1
            
        start_day += 1
        
    return ans



want = ["banana", "apple", "rice", "pork", "pot"]	
number = [3, 2, 2, 2, 1]	
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print(solution(want, number, discount))