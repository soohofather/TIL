sum_n = 0
n_list = []

for _ in range(10):
    n = int(input())

    sum_n += n
    n_list.append(n)

cnt = 0
result = 0

for i in n_list:
    if n_list.count(i) > cnt:
        cnt = n_list.count(i)
        result = i

print(format(sum_n / 10, '.0f'), result)



