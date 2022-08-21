case = 0
while True:
    use, day, vac = map(int, input().split())
    if use + day + vac == 0:
        break
    if vac % day < use:
        ans = use * (vac // day) + (vac % day)
    else:
        ans = use * (vac // day) + use
    case += 1
    print("Case %d:" %case, ans)