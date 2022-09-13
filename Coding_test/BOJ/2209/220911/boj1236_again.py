a, b = map(int, input().split())

temple = []
cnt_a = 0

for _ in range(a):
    check = input()
    temple.append(check)
    if 'X' not in check:
        cnt_a += 1

cnt_b = 0
for i in range(b):
    for ii in range(a):
         if temple[ii][i] == 'X':
            break
    else:
        cnt_b += 1
print(cnt_a if cnt_a > cnt_b else cnt_b)