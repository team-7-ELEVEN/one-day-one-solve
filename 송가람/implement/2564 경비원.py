r, c = map(int, input().split())
store = [list(map(int, input().split())) for _ in range(int(input()))]
me = list(map(int, input().split()))

# 북_서 or 서_북
def n_w(n, w):
    return n + w

# 북_동 or 동_북
def n_e(n, e):
    return (r - n) + e

# 북_남 or 남_북
def n_s(n, s):
    return min((n + c + s),((r - n) + c + (r - s)))

# 서_남 or 남_서
def w_s(w, s):
    return (c - w) + s

# 남_동 or 동_남
def e_s(e, s):
    return (c - e) + (r - s)

# 서_동 or 동_서
def w_e(w, e):
    return min((w + r + e),((c - e) + r + (c - w)))

ans = 0
d2, l2 = me
for i in store:
    d1, l1 = i
    # 내가 북
    if d2 == 1:
        if d1 == 1:
            ans += abs(l1 - l2)
        elif d1 == 2:
            ans += n_s(l2, l1)
        elif d1 == 3:
            ans += n_w(l2, l1)
        elif d1 == 4:
            ans += n_e(l2, l1)
    # 내가 남
    elif d2 == 2:
        if d1 == 1:
            ans += n_s(l1, l2)
        elif d1 == 2:
            ans += abs(l1 - l2)
        elif d1 == 3:
            ans += w_s(l1, l2)
        elif d1 == 4:
            ans += e_s(l1, l2)
    # 내가 서
    elif d2 == 3:
        if d1 == 1:
            ans += n_w(l1, l2)
        elif d1 == 2:
            ans += w_s(l2, l1)
        elif d1 == 3:
            ans += abs(l1 - l2)
        elif d1 == 4:
            ans += w_e(l2, l1)
    # 내가 동
    elif d2 == 4:
        if d1 == 1:
            ans += n_e(l1, l2)
        elif d1 == 2:
            ans += e_s(l2, l1)
        elif d1 == 3:
            ans += w_e(l1, l2)
        elif d1 == 4:
            ans += abs(l1 - l2)

print(ans)

