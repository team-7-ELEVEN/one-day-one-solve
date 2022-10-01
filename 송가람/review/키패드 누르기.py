
def solution(numbers, hand):
    def distance(a, b):
        return abs(table[a][0] - table[b][0]) + abs(table[a][1] - table[b][1])
    
    ans = ""
    table = {}
    i = 0
    n = 1
    
    for _ in range(3):
        for j in range(3):
            table[n] = [i, j]
            n += 1
        i += 1
        
    table["*"] = [3, 0]
    table[0] = [3, 1]
    table["#"] = [3, 2]
    
    left_hand = "*"
    right_hand = "#"
    
    for i in numbers:
        if i in [1, 4, 7]:
            ans += "L"
            left_hand = i
        elif i in [3, 6, 9]:
            ans += "R"
            right_hand = i
        elif i in [2, 5, 8, 0]:
            if distance(i, left_hand) > distance(i, right_hand):
                ans += "R"
                right_hand = i
            elif distance(i, left_hand) == distance(i, right_hand):
                if hand == "left":
                    ans += "L"
                    left_hand = i
                else:
                    ans += "R"
                    right_hand = i
            else:
                ans += "L"
                left_hand = i
    
    return ans