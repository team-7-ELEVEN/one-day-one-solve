t=int(input())

def check(front,rear,lst):
    while front<rear:
        if lst[front]==lst[rear]:
            front+=1
            rear-=1
        else:
            return False
    return True

for _ in range(t):
    lst=input()
    front=0
    rear=len(lst)-1
    cnt=0
    if lst==lst[::-1]:
        print(0)
        continue
    else:
        while front<rear:
            if lst[front]==lst[rear]:
                front+=1
                rear-=1
            else:
                one=check(front+1,rear,lst)
                two=check(front,rear-1,lst)
                if one or two:
                    print(1)
                    break
                else:
                    print(2)
                    break
