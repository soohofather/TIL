n = int(input())

condo = []

for i in range(n):
    packs = input()
    condo.append(packs)

garo = 0
cnt_garo = 0

for ii in range(n):
    for iii in range(n):
        if condo[ii][iii] == '.':
            cnt_garo += 1
        elif condo[ii][iii] == 'X':
            if cnt_garo >= 2:
                garo += 1
                cnt_garo = 0
            else:
                cnt_garo = 0
    else:
        if cnt_garo >= 2:
            garo += 1
            cnt_garo = 0
        else:
            cnt_garo = 0

sero = 0
cnt_sero = 0

for iiii in range(n):
    for iiiii in range(n):
        if condo[iiiii][iiii] == '.':
            cnt_sero += 1
        elif condo[iiiii][iiii] == 'X':
            if cnt_sero >= 2:
                sero += 1
                cnt_sero = 0
            else:
                cnt_sero = 0
    else:
        if cnt_sero >= 2:
            sero += 1
            cnt_sero = 0
        else:
            cnt_sero = 0

print(garo, sero)
