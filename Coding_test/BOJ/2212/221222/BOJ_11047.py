n, k = map(int, input().split())

money_list = []

for _ in range(n):
    money_list.append(int(input()))

money_list.sort(reverse=True)

result = 0

for money in money_list:

    result += k // money
    k %= money

print(result)
