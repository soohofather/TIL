T = int(input())

people = []

for _ in range(T):
    numbers = list(map(int, input().split()))
    people.append(numbers)

result = 1

for i in people:
    for ii in people:
        if i[0] < ii[0] and i[1] < ii[1]:
            result += 1
    print(result)
    result = 1