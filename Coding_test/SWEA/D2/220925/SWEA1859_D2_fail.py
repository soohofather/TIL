TC = int(input())

for _ in range(1, TC + 1):

    T = int(input())
    numbers = list(map(int, input().split()))

    sell_price = 0
    wallet = 0

    for i in numbers[::-1]:
        if i >= sell_price:
            sell_price = i
        else:
            wallet += sell_price - i
    print(f'#{_}', wallet)