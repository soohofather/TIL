cow = []

for _ in range(11):
    cow.append(2)

cnt = 0

T = int(input())

for _ in range(T):
    cow_number, where = map(int, input().split())
    if where == cow[cow_number]:
        continue
    elif where != cow[cow_number]:
        if cow[cow_number] == 2:
            cow[cow_number] = where
        else:
            cow[cow_number] = where
            cnt += 1
print(cnt)
