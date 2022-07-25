number = 123
result = 0

while number:
    result *= 10
    result += number%10
    number //= 10

print(result)
