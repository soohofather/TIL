sentence = input()

print(sentence[0], end='')
for i in range(1, len(sentence)):
    if sentence[i] == '_':
        print('_', end='')
    elif sentence[i] == '.':
        print('.', end='')
    else:
        print(chr(ord(sentence[i]) - 32), end='')