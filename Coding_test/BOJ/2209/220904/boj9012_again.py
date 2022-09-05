import sys

sys.stdin = open('test.txt')

TC = int(input())

cnt = 0

for _ in range(TC):
    gwalho = input()
    for i in gwalho:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:
                print('NO')
                break
            else:
                cnt -= 1
    else:
        print('YES' if cnt == 0 else 'NO')
        cnt = 0