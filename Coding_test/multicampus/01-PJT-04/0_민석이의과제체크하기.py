import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

result = []

for _ in range(1, T + 1):
    students, done = map(int, input().split())
    student_done = list(map(int, input().split()))
    print(f'#{_}', end=' ')
    for i in range(1, students+1):
        if i not in student_done:
            print(i, end=' ')
    print()


