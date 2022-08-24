import heapq

n = int(input())
lec = []
for _ in range(n):
    lec.append(list(map(int, input().split())))

lec.sort()
room = []
heapq.heappush(room, lec[0][1])

for i in range(1, n):
    if room[0] > lec[i][0]:
        heapq.heappush(room, lec[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, lec[i][1])
        
print(len(room))
