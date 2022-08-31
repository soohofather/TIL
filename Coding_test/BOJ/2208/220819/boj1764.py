T1, T2 = map(int, input().split())

no_see = {}

for i in range(T1):
    saram1 = input()
    if saram1 not in no_see:
        no_see[saram1] = 1
    else:
        no_see[saram1] += 1

for ii in range(T2):
    saram2 = input()
    if saram2 not in no_see:
        no_see[saram2] = 1
    else:
        no_see[saram2] += 1

result = []

for iii in no_see:
    if no_see[iii] == 2:
        result.append(iii)

result.sort()

print(len(result))

for _ in range(len(result)):
    print(result[_])