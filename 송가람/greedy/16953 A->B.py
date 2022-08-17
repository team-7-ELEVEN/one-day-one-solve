import sys
input = sys.stdin.readline
n, goal = map(int, input().split())
cnt = 0

while True:
    str_goal = str(goal)
    if goal == n:
        print(cnt + 1)
        break
    elif goal <= n:
        print(-1)
        break

    if goal % 2 == 0:
        goal = goal // 2
        cnt += 1
    elif goal % 2 == 1:
        if str_goal[-1] == "1":
            goal = int(str_goal[:-1])
            cnt += 1
        else:
            print(-1)
            break

   

