TC = int(input())

for _ in range(TC):
    a, b = input().split()
    result = ''
    for i in range(len(b)):
        if i == (int(a) - 1):
            continue
        else:
            result += b[i]
    print(result)