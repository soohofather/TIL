import sys

sys.stdin = open("test.txt")


TC = int(input())

for _ in range(1, TC + 1):
    print(f"#{_}")
    money = int(input())

    bill = {
        50000: 0,
        10000: 0,
        5000: 0,
        1000: 0,
        500: 0,
        100: 0,
        50: 0,
        10: 0,
    }

    for i in bill:
        if i <= money:
            cnt = money // i
            money -= i * cnt
            bill[i] += cnt
        print(bill[i], end=" ")
    print()
