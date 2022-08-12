import sys


sys.stdin = open("_Flatten.txt")

for _ in range(1, 11):

    T = int(input())

    numbers = list(map(int, input().split()))
    numbers.sort()

    for i in range(T):
        if max(numbers)-min(numbers) < 2:
            break 
        numbers.append(numbers.pop() - 1)
        numbers.append(numbers.pop(0) + 1) 
        numbers.sort()
    print(f'#{_}', max(numbers)-min(numbers))
