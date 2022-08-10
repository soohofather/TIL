result = [[],[]]

for i in range(2):
    for ii in range(10):
        result[i].append(int(input()))
    result[i].sort(reverse = True)

final_result = [0, 0]

for i in range(2):
    for ii in range(3):
        final_result[i] += result[i][ii]
    print(final_result[i], end=(' '))