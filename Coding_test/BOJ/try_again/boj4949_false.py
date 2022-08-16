import sys
sys.stdin = open('boj4949.txt')

Q = ''

while Q != '.':
    Q = input().rstrip()
    if Q == '.':
        break
    so = []
    dae = []

    for i in input():

        if i == '(':
            so.append(i)
        elif i == ')':
            if len(so) == 0:
                so.append(i)
            else:
                so.pop(so.index('('))
        elif i == '[':
            dae.append(i)
        elif i == ']':
            if len(dae) == 0:
                dae.append(i)
            else:
                dae.pop(dae.index('['))
    print('yes' if len(so) == 0 and len(dae) == 0 else 'no')
