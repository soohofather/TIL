
a = 123
m = 0

while a > 0:
    b = a % 10
    m += b
    a //= 10

print(m)