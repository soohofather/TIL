import sys

sys.stdin = open("test.txt")

TC = int(input())
for _ in range(1, TC + 1):

    n, k = map(int, input().split())

    puzzle = []

    for i in range(n):
        whiteblack = list(map(int, input().split()))
        puzzle.append(whiteblack)

    cnt = 0

    for garo in range(n):
        check = 0
        for ii in range(n):
            if puzzle[garo][ii] == 1:
                check += 1
            else:
                if check == k:
                    cnt += 1
                    check = 0
                else:
                    check = 0
        if check == k:
            cnt += 1

    for sero in range(n):
        check = 0
        for iii in range(n):
            if puzzle[iii][sero] == 1:
                check += 1
            else:
                if check == k:
                    cnt += 1
                    check = 0
                else:
                    check = 0
        if check == k:
            cnt += 1
    print(f"#{_}", cnt)
w
