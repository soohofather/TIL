TC = int(input())

result = {}

for _ in range(TC):
    name = input()
    if name not in result:
        result[name] = 1
    else:
        result[name] += 1

for _ in range(TC-1):
    result[input()] -= 1

for i in result:
    if result[i] == 1:
        print(i)
        break

