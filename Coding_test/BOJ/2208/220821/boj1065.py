
n = int(input())
a = 1
cnt = 0

while a <= n:
    if a < 100:
        cnt += 1
    else:
        if int(str(a)[1]) - int(str(a)[0]) == int(str(a)[2]) - int(str(a)[1]):
            cnt += 1
    a += 1
print(cnt)
