import sys

sys.stdin = open('test.txt')

saram = int(input())

points = [[],[],[]]                         # 첫판에 낸 숫자, 두번째 판에 낸 숫자, 세번째 판에 낸 숫자를 모아서
                                            # 해당 숫자를 그 판에 똑같은게 있는지를 찾는 방향으로 접근
for i in range(saram):
    a, b, c = map(int, input().split())
    points[0].append(a)
    points[1].append(b)
    points[2].append(c)

result = 0

for ii in range(saram):
    for iii in range(3):
        if points[iii].count(points[iii][ii]) == 1:     # 찾는 점수가 그 그룹안에서 카운트를하여 카운트 값이 1이면 그 해당 점수를 result에 추가
            result += points[iii][ii]                   # 즉, 결과 값이 1은 그 숫자가 1개라는 의미이고, 2이상은 같은 숫자가있다는 것을 의미
    print(result)
    result = 0