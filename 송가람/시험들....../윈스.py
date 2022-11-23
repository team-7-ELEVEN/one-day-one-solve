def solution(n):
    ans = []
    # n =[ str(i) for i in n ]
    nums = []
    max_len = 0
    for i in n:
        str_n = str(i)
        nums.append(str_n)
        if max_len < len(str_n):
            max_len = len(str_n)

    print(max_len)

    for s in nums:
        d = max_len - len(s)
        new_s = ("0" * d) + s
        ans.append(new_s)

    print(ans)

solution(
[0, 6789, 999])
