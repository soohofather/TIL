a, b = map(int, input().split())

x = abs((a // 4 if a % 4 == 0 else (a // 4) + 1) - (b // 4 if b % 4 == 0 else (b // 4) + 1))
y = abs((a % 4 if a % 4 != 0 else 4) - (b % 4 if b % 4 != 0 else 4))

print(x + y)
