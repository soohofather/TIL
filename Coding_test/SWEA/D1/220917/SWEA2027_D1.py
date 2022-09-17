
for ii in range(5):
    result = ''
    for i in range(5):
        if ii == i:
            result += '#'
        else:
            result += '+'
    print(result)

