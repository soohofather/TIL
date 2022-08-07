import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    ground = []

    for i in range(N):
        numbers = list(map(int, input().split()))
        ground.append(numbers)

    flies = []
    result = 0
    moving = 0

    for d in range(0, N - M + 1):
        for c in range(0, N - M + 1):
            for a in range(0 + d, M + d):
                for b in range(0 + moving, M + moving):
                    flies.append(ground[a][b]) 
            moving += 1
            if sum(flies) > result:
                result = sum(flies)
            flies = []
        moving = 0
    print(f'#{_ + 1}', result)
