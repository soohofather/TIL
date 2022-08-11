X, N = int(input()), int(input())

Y = 0

for i in range(N):
    a, b = map(int, input().split())
    Y += a * b
print('Yes' if X == Y else 'No')

