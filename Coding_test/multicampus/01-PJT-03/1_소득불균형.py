import sys

sys.stdin = open("_소득불균형.txt")

T1 = int(input())

for i in range(T1):
    
    T2 = input()
    numbers = list(map(int, input().split()))

    average = sum(numbers) / len(numbers)
    result = 0

    for ii in numbers:
        if average >= ii:
            result += 1
    print(f'#{i+1}', result)