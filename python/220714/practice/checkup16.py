findyou = input()
moum = ('a', 'e', 'i', 'o', 'u')
result = 0

for gesu in findyou:
    for gesu2 in moum:
        if gesu == gesu2:
            result += 1
print(result)