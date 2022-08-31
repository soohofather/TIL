result = 0

for i in range(10):
    number = int(input())
    if i == 0:
        result = number
    elif abs(result - 100) > abs(result + number - 100):
        result += number
    elif abs(result - 100) == abs(result + number - 100):
        result += number
        break
    elif abs(result - 100) < abs(result + number - 100):
        break
print(result)
