
cnt = 1
result = 1

for _ in range(3):
    number = input()
    for i in range(0, 7):
        if number[i] != number[i + 1]:
            cnt = 1
            if cnt > result:
                result = cnt
        else:
            cnt += 1
            if cnt > result:
                result = cnt
    print(result)
    cnt = 1
    result = 1