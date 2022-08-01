T = int(input())

number_list = []

for i in range(T):
    number = int(input())

    if number == 0:
        number_list.pop()
    else:
        number_list.append(number)

print(sum(number_list))
