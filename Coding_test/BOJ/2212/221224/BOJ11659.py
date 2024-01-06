n, m = map(int, input().split())

numbers = list(map(int, input().split()))

new_numbers = [0]

count = 0

for i in range(n):
    count += numbers[i]
    new_numbers.append(count)

for _ in range(m):
    a, b = map(int, input().split())
    result = new_numbers[b] - new_numbers[a - 1]
    print(result)