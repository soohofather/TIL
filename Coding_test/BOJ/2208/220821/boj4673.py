number_list = []
n = 1

while n < 10001:
    m = str(n)
    o = 0
    for i in range(len(m)):
        o += int(m[i])
    else:
        number_list.append(n + o)
        n += 1

for ii in range(1, 10001):
    if ii not in number_list:
        print(ii)