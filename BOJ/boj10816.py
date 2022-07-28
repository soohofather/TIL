import sys

sys.stdin = open('boj10816.txt')


T1 = input()
card_numbers = input().split()

T2 = input()
find_numbers = input().split()

count_numbers = {}

for i in card_numbers:
    if i in count_numbers:
        count_numbers[i] += 1
    else:
        count_numbers[i] = 1

for ii in find_numbers:
    print(count_numbers.get(ii, 0), end=(' '))