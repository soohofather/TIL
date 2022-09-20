TC = int(input())


festival_1 = {
    1: 5000000,
    2: 3000000,
    3: 2000000,
    4: 500000,
    5: 300000,
    6: 100000
    }

festival_2 = {
    1: 5120000,
    2: 2560000,
    4: 1280000,
    8: 640000,
   16: 320000,
}

for _ in range(TC):
    a, b = map(int, input().split())
    cnt_1 = 0
    cnt_2 = 0
    result = 0
    for i in festival_1:
        cnt_1 += i
        if a == 0:
            break
        elif cnt_1 >= a:
            result += festival_1[i]
            break
    for ii in festival_2:
        cnt_2 += ii
        if b == 0:
            break
        elif cnt_2 >= b:
            result += festival_2[ii]
            break
    print(result)