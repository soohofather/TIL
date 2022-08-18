star = int(input())

for stars in range(1, star +1):
    if stars % 2 == 1:
        for i in range(1, star * 2):
            if i % 2 == 1:
                print('*', end=(''))
            else:
                print(' ', end=(''))
        else:
            print('')
    else:
        for i in range(1, star * 2 + 1):
            if i % 2 == 1:
                print(' ', end=(''))
            else:
                print('*', end=(''))
        else:
            print('')