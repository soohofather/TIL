number_list = []
total = 0

for i in range(5):
    number = int(input())
    number_list.append(number)
    total += number 
number_list.sort()
print(total // 5)
print(number_list[2])

