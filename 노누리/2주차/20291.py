n=int(input())
extension={}

for _ in range(n):
    name,ex=input().split('.')
    if ex not in extension:
        extension[ex]=0
    extension[ex]+=1

set_ex=sorted(extension)
for se in set_ex:
    print(se,extension[se])
