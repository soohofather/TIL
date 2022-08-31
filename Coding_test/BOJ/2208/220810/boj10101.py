a, b, c = int(input()), int(input()), int(input())

if a + b + c == 180:
    if a == b and b == c:
        print('Equilateral')
    elif a != b and a != c and b != c:
        print('Scalene')
    else:
        print('Isosceles')
else:
    print('Error')