
A, B, C = map(int, input().split())

parking = []

for i in range(3):
    a, b = map(int, input().split())
    for ii in range(a, b):
        parking.append(ii)

fee = 0

for iii in range(min(parking), max(parking) + 1):
    if parking.count(iii) == 1:
        fee += (1 * A)
    elif parking.count(iii) == 2:
        fee += (2 * B)
    elif parking.count(iii) == 3:
        fee += (3 * C)
print(fee)