
fruit = input()
dict = {}

for findyou in fruit:
    if findyou in dict:
        dict[findyou] += 1
    else:
        dict[findyou] = 1
print(dict)

print(dict.items())             # 튜플이 되었음

for a, b in dict.items():       # 그 튜플을 쌍쌍히 출력 됨
    print(a, b)
