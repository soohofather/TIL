T = int(input())

for i in range(T):
    list = int(input())
    m = 0

    for ii in range(1, list + 1):
        if ii % 2 == 1:
            m += ii
        else:
            m -= ii
    print(f'#{i+1}', m)