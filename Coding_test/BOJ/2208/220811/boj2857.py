cnt = 0

for i in range(1,6):
    fbi = input()
    if 'FBI' in fbi:
        cnt += 1
        print(i, end=(' '))
else:
    if cnt == 0:
        print('HE GOT AWAY!')
