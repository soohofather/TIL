import sys

sys.stdin = open("_반반.txt")

TC = int(input())

test_list = []

for _ in range(1, TC + 1):
    alphabet = input()
    for i in alphabet:
        test_list.append(i)
    test_list.sort()
    if test_list[0:2] == test_list[2:4]:
        print(f'#{_} No')
    else:
        if test_list[0] == test_list[1] and test_list[2] == test_list[3]:
            print(f'#{_} Yes')
        else:
            print(f'#{_} No')
    test_list = []