T = int(input())

for i in range(1, T + 1):
    numbers = list(map(int, input().split()))
    result = 0
    for ii in numbers:
        if ii % 2:
            result += ii
    print(f'#{i}', result)
