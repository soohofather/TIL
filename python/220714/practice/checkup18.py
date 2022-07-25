fruit = input()
dict = {}

for gaesu in fruit:
    if gaesu in dict:
        dict[gaesu] += 1
    else:
        dict[gaesu] = 1

for gaesu1,gaesu2 in dict.items():
    print(gaesu1, gaesu2)