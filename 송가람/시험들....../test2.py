import heapq
def solution(K, user_scores):
    n = []
    heap = []
    cnt = 0
    for i in user_scores:
        name, score = i.split()
        if not heap:
            n.append(name)
            heapq.heappush(heap, [int(score), name])
            cnt += 1
        else:
            flag = False
            if name in n:
                h = []
                while heap:
                    p = heapq.heappop(heap)
                    if p[0] < int(score):
                        if flag:
                            cnt += 1
                            flag = False
                        if p[1] == name:
                            heapq.heappush(h, [int(score), name])
                            flag = True
                        else:
                            heapq.heappush(h, [p[0], p[1]])
                    else:
                        heapq.heappush(h, [p[0], p[1]])
                heap = h
            else:
                p = heapq.heappop(heap)
                n.remove(p[1])
                if p[0] < int(score):
                    heapq.heappush(heap, [int(score), name])
                    n.append(name)
                    cnt += 1
                    if len(heap) < K:
                        heapq.heappush(heap, [p[0], p[1]])
                        n.append(p[1])
                else:
                    heapq.heappush(heap, [p[0], p[1]])
                    n.append(p[1])
    print(heap)
    return cnt



print(solution(3, ["alex111 100", "cheries2 200", "coco 150", "luna 100", "alex111 120", "coco 300", "cheries2 110"]))
