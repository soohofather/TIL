TC = int(input())

milk_shop = list(map(int, input().split()))

result = 0
milk_status = 0

for i in milk_shop:
    if i != milk_status:
        continue
    else:
        if milk_status == 2:
            milk_status = 0
            result += 1
        else:
            milk_status += 1
            result += 1
print(result)