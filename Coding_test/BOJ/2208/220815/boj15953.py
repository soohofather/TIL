def first(number):
    if number == 0:
        return 0
    elif number == 1:
        return 5000000
    elif number <= 3:
        return 3000000
    elif number <= 6:
        return 2000000
    elif number <=10:
        return 500000
    elif number <= 15:
        return 300000
    elif number <= 21:
        return 100000
    else:
        return 0

def second(number):
    if number == 0:
        return 0
    elif number == 1:
        return 5120000
    elif number <= 3:
        return 2560000
    elif number <= 7:
        return 1280000
    elif number <=15:
        return 640000
    elif number <= 31:
        return 320000
    else:
        return 0

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    print(first(a) + second(b))