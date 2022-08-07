import sys

sys.stdin = open("_문자열의거울상.txt")

T1 = int(input())

for _ in range(T1):

    moonja = input()
    result = ''

    for i in moonja:
        if i == 'b':
            result += 'd'
        elif i == 'd':
            result += 'b'
        elif i == 'p':
            result += 'q'
        elif i == 'q':
            result += 'p'
    print(f'#{_+1}', result[::-1])
