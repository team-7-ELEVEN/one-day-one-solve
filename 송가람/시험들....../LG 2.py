def solution(k, limits, sockets):
    # for flags in sockets:
    #     for flag in flags:
    
    def calculate_power(n, cnt):
        power = 0
        for flag in sockets[n - 1]:
            if flag == -1:
                power += k
            elif flag > 0:
                power += calculate_power(flag, cnt)
        if power > limits[n - 1]:
            while power <= limits[n - 1]:
                power -= k
                cnt += 1
        return power, 

    


k = 300
limits = [2000, 1000, 3000, 200, 600, 500]
sockets = [[2, 3, -1, -1, -1], [4, 0, -1, -1, 6], [5, 0, 0, 0, 0], 
[-1, 0, 0, 0, 0], [-1, -1, -1, -1, -1], [-1, -1, 0, 0, 0]]