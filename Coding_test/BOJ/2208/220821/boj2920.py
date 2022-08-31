numbers = list(map(int, input().split()))

result = ''

if numbers[0] == 1:
    for i in range(7):
        if numbers[i] + 1 == numbers[i + 1]:
            result = 'ascending'
            continue
        else:
            result = 'mixed'
            break
elif numbers[0] == 8:
    for i in range(7):
        if numbers[i] - 1 == numbers[i + 1]:
            result = 'descending'
            continue
        else:
            result = 'mixed'
            break
else:
    result = 'mixed'
print(result)