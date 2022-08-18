from collections import deque

number = int(input())

numbers = deque(range(1, number + 1))

while len(numbers) > 1:
    print(numbers.popleft(), end=' ')
    numbers.append(numbers.popleft())

print(numbers[0])