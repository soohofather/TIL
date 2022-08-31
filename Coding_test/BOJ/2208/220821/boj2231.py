n = int(input())

start = 1

while True:

    result = 0

    for i in range(len(str(start))):
        result += int(str(start)[i])
    else:
        if start + result == n:
            print(start)
            break
        elif start == n:
            print(0)
            break
    start += 1