arr = []
for _ in range(int(input())):
    age, name = input().strip().split()
    arr.append((int(age), name))

sorted_arr = sorted(arr, key=lambda x: x[0])

for i in sorted_arr:
    age, name = i
    print(age, name)
