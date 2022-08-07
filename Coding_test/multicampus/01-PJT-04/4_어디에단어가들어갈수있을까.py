import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())

for _ in range(1, T + 1):

    M, K = map(int, input().split())

    puzzle = []

    for i in range(M):
        numbers = list(map(int, input().split()))
        puzzle.append(numbers)

    garo = 0
    cnt_garo = 0

    for i in range(M):
        for ii in range(M):
            if puzzle[i][ii] == 1:
                cnt_garo += 1
            elif puzzle[i][ii] == 0:
                if cnt_garo == K:
                    garo += 1
                    cnt_garo = 0
                else:
                    cnt_garo = 0
        else:
            if cnt_garo == K:
                garo += 1
                cnt_garo = 0
            else:
                cnt_garo = 0

    sero = 0
    cnt_sero = 0

    for i in range(M):
        for ii in range(M):
            if puzzle[ii][i] == 1:
                cnt_sero += 1
            elif puzzle[ii][i] == 0:
                if cnt_sero == K:
                    sero += 1
                    cnt_sero = 0
                else:
                    cnt_sero = 0
        else:
            if cnt_sero == K:
                sero += 1
                cnt_sero = 0
            else:
                cnt_sero = 0
    print(f'#{_}', garo+sero)