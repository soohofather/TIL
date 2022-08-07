import sys

sys.stdin = open("_암호생성기.txt")

for _ in range(10):

    T = int(input())
    numbers = list(map(int, input().split()))

    cnt = 1

    while numbers[7] != 0:
        if cnt == 6:
            cnt = 1
        elif numbers[0] - cnt <  0:
            push_number = numbers.pop(0)
            numbers.append(0)
        else:
            push_number = numbers.pop(0)
            numbers.append(push_number - cnt)
            cnt += 1
    print(f'#{T}', end=' ')
    for n in numbers:
        print(n, end=' ')
    print()
