T = int(input())
for i in range(1, T + 1):

    TC = int(input())
    print(f'#{i}')

    result = ''

    for _ in range(TC):
        a, b = input().split()
        for _ in range(int(b)):
            if len(result) != 10:
                result += a
            else:
                print(result)
                result = ''
                result += a
    print(result)
