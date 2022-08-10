number = int(input())
new_number = str(number)
len_number = 0

for i in range(number):
    for ii in range(len(str(number - i))):
        if str(number - i)[ii] in ['4', '7']:
            len_number += 1
        else:
            break
    if len_number == len(str(number - i)):
        print(number - i)
        break
    else:
        len_number = 0
