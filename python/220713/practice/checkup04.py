# 주어진 리스트의 요소 중에서 5의 개수를 출력하시오.
# print(numbers.count(5))

numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

n = 5
gaesu = 0

for number in numbers:
    if number == n:
        gaesu = gaesu + 1

print(gaesu)