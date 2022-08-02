
N = int(input())

for i in range(N):
    r, e, c = map(int, input().split())
    ec = e - c
    if r > ec:
        print('do not advertise')
    elif r == ec:
        print('does not matter')
    elif r < ec:
        print('advertise')