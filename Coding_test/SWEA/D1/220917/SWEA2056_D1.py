
TC = int(input())

for _ in range(1, TC+1):
    numbers = input()
    year = numbers[:4]
    month = numbers[4:6]
    day = numbers[6:]
    if int(year) == 0:
        print(f'#{_} -1')
        continue 
    elif int(month) == 0 or int(month) > 12:
        print(f'#{_} -1')
        continue
    elif month in ['01', '03', '05', '07', '08', '10', '12']:
        if int(day) == 0 or int(day) > 31:
            print(f'#{_} -1')
            continue
    elif month in ['04', '06', '09', '11']:
        if int(day) == 0 or int(day) > 30:
            print(f'#{_} -1')
            continue
    elif month == '02':
        if int(day) == 0 or int(day) > 28:
            print(f'#{_} -1')
            continue
    print(f'#{_} {year}/{month}/{day}')