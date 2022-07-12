numbers = [3, 10, 20]
plus = 0
hab = 0

for idx in numbers:
    hab += numbers[plus]
    plus += 1
else:
    print(hab / plus)

