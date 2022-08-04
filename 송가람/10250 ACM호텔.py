def making_room(H, W):
    rooms = []
    for i in range(1, W + 1):
        for j in range(1, H + 1):
            rooms.append((100 * j) + i)
    return rooms


n = int(input())
for i in range(n):
    H, W, N = map(int, input().split())
    print(making_room(H, W)[N - 1])





