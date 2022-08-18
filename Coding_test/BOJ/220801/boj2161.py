number = int(input())

numbers = list(range(1, number + 1))

while len(numbers) > 1:
    print(numbers.pop(0), end = ' ')
    numbers.append(numbers.pop(0))

print(numbers[0])