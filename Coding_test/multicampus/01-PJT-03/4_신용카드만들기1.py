import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())

for _ in range(T):

    card_numbers = list(map(int, input().split()))

    result = 0

    for i in range(0, 15):
        if i % 2 == 1:
            result += card_numbers[i]
        else:
            result += (card_numbers[i] * 2)
    print(f'#{_+1}',10-(result % 10) if 10-(result % 10) != 10 else 0)

