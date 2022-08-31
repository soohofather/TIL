T = int(input())

cups = [0, 1, 2, 3]

for _ in range(T):
    x, y = map(int, input().split())
    a = cups[x]
    b = cups[y]
    cups[y] = a
    cups[x] = b
print(cups.index(1))
