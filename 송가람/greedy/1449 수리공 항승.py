# 지운님은 천재야..
n, l = map(int, input().split())
pipe = list(map(int, input().split()))
pipe.sort()

idx = 0
cnt = 0
while pipe:
    if idx >= len(pipe):
        cnt += 1
        break
    if pipe[idx] < pipe[0] + l:
        idx += 1
    else:
        pipe = pipe[idx:]
        cnt += 1
        idx = 0

print(cnt)