book_number,dummy_number = map(int, input().split())

result = 'Yes'

for i in range(dummy_number):
    a = int(input())
    numbers = list(map(int, input().split()))
    for ii in range(a - 1):
        if numbers[ii] < numbers[ii + 1]:
            result = 'No'
            break
    if result == 'No':
        break
print(result)
