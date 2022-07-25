number = int(input())

for i in range(1, number + 1):
    n = i * '*'
    m = (number - i) * ' '
    print(m, n, sep=(''))