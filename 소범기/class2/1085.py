list_ =[ int(x) for x in input().split()]
target = min(min(list_[0],list_[2]-list_[0]),min(list_[1],list_[3]-list_[1]))
print(target)