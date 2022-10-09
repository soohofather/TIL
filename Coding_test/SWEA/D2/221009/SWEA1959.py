TC = int(input())

for _ in range(1, TC + 1):

    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n > m:
        n, m = m, n
        a, b = b, a

    result = 0
    real_result = 0

    for i in range(m - n + 1):
        for ii in range(n):
            result += a[ii] * b[ii + i]
        if result > real_result:
            real_result = result
            result = 0
        else:
            result = 0
    print(f"#{_}", real_result)
