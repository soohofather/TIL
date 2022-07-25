fruit = input()
result = -1
char = ''

for gottacha in fruit:
    result += 1
    if gottacha == 'a':
        char += str(result) + ' '
print(char)


