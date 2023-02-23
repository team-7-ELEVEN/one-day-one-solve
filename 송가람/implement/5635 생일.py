n = int(input())
people = []

for _ in range(n):
    name, d, m, y = input().split()
    
    people.append([name, int(d), int(m), int(y)])

people.sort(key=lambda x: (x[3], x[2], x[1]))

print(people[-1][0])
print(people[0][0])
