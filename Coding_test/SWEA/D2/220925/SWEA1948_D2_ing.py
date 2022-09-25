month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31, 
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

TC = int(input())
for tc in range(1, TC + 1):

    numbers = list(map(int, input().split()))

    result = 0

    for i in range(numbers[0], numbers[2] + 1):
        if i == numbers[0]:
            result += month[numbers[0]] - numbers[1] + 1
        elif i == numbers[2]:
            result += numbers[3]
        else:
            result += month[i]
    print(f'#{tc}', result)