import sys

sys.stdin = open("SWEA1954.txt")

TC = int(input())

for n in range(1, TC + 1):
    print(f"#{n}")

    T = int(input())

    snail = [[[0] for _ in range(T)] for __ in range(T)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]  # 0 = >>, 1 = 아래로, 2 = >>, 3 = 위로

    x = 0
    y = 0
    narrow = 0

    for i in range(1, (T * T) + 1):

        snail[x][y] = i

        x += dx[narrow]
        y += dy[narrow]

        if x < 0 or y < 0 or x >= T or y >= T or snail[x][y] != [0]:
            x -= dx[narrow]
            y -= dy[narrow]

            narrow = (narrow + 1) % 4
            x += dx[narrow]
            y += dy[narrow]

    for ii in snail:
        for iii in ii:
            print(iii, end=" ")
        print()
