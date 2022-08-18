import sys

sys.stdin = open('test.txt')

N, M = map(int, input().split())

numbers = []

for a in range(N):
    numbers.append(list(map(int, input().split())))

K = int(input())

for b in range(K):
    i, j, x, y = map(int, input().split())
    result = 0
    for c in range(x - i + 1):                          # 시작기준을 정하고 필요한 만큼만 돌게하면 될 것같은? 느낌을 받았습니다.
        for d in range(y - j + 1):                      # 몇번을 돌게하는건 두개의 숫자의 차이만큼 돌아야하는데, range가 -1을 받아서 +1을 해줌.
            result += numbers[i - 1 + c][j - 1 + d]     # 처음 시작하는 기준을 문제에서 좌표로 되어있어서 이것을 인덱스 위치로 바꾸고
    print(result)                                       # 기준점에서 처음 몇번 돌릴지 정한 숫자만큼 돌리게 하는 방법
                                                        # 음.. 설명을 적어놨지만.. 내가 읽어도 어려운거같네..