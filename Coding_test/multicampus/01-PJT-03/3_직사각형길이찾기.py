import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())

for _ in range(T):

    a, b, c = list(map(int, input().split()))
    d = 0

    if a == b and b == c:
        d += a
    elif a == b and a != c:
        d += c
    elif a != b and a == c:
        d += b
    elif a != b and b == c:
        d += a

    print(f'#{_+1}', d)

