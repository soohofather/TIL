import sys

sys.stdin = open("_모음이보이지않는사람.txt")

moum = 'aeiou'

TC = int(input())
result = ''

for _ in range(1, TC + 1):
    sentence = input()
    for i in range(len(sentence)):
        if sentence[i] in moum:
            continue
        else:
            result += sentence[i]
    print(f'#{_}', result)
    result = ''
