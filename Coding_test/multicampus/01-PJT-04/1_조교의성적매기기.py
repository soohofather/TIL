import sys

sys.stdin = open("_조교의성적매기기.txt")

degree = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())

for _ in range(1, T + 1):

    students, my_degree = map(int, input().split())

    result = []
    grade = 0

    for i in range(1, students + 1):
        a, b, c = map(int, input().split())
        result.append((a*0.35) + (b*0.45) + (c*0.2))
    new_result = sorted(result, reverse = True)
    print(f'#{_}', degree[new_result.index(result[my_degree - 1]) // (students // 10)])


