findyou = input()
result = 0

for gesu in findyou:
    if gesu in ('a', 'e', 'i', 'o', 'u'):
        result += 1
print(result)