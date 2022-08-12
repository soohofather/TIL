import sys

sys.stdin = open("_퍼펙트셔플.txt")

TC = int(input())

for _ in range(1, TC + 1):
    T = int(input())

    quiz = list(input().split())

    A_list = []
    B_list = []

    cnt = (T // 2) if T % 2 == 0 else (T // 2) + 1

    for i in range(cnt):
        A_list.append(quiz[i])

    for ii in range(cnt, len(quiz)):
        B_list.append(quiz[ii])

    result = []

    if len(A_list) == len(B_list):
        for iii in range(len(B_list)):
            result.append(A_list[iii])
            result.append(B_list[iii])
    else:
        for iii in range(len(B_list)):
            result.append(A_list[iii])
            result.append(B_list[iii])
        else:
            result.append(A_list[len(A_list) - 1])
    print(f'#{_}', end=(' '))
    for iiii in result:
        print(iiii, end=(' '))
    print()