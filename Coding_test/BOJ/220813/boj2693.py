T = int(input())

for _ in range(T):
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(numbers[-3])
