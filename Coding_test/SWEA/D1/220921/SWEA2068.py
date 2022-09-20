T = int(input())

for i in range(1, T + 1):
    numbers = list(map(int, input().split()))
    numbers.sort()
    result = numbers.pop()
    print(f'#{i}', result)
