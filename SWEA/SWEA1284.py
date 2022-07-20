T = int(input())

for i in range(T):
    l = list(map(int, input().split()))
    A = 0
    B = 0

    A = l[0] * l[4]

    if l[4] <= l[2]:
        B = l[1]
    else:
        B = l[1] + l[3] * l[4]- l[3] * l[2]

    print(f'#{i + 1}', A if A < B else B)