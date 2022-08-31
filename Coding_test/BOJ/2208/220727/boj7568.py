import sys

sys.stdin = open('boj7598.txt')

T = int(input())

result = []

for i in range(T):
    body = kg, cm = list(map(int, input().split()))
    result.append(body)                                # print(result) = [[55, 185], [58, 183], [88, 186], [60, 175], [46, 155]]

for ii in result:
    cnt = 1                                            # 다른 사람과 비교하여 다른사람이 더 크면 +1(등수 1등 추가의미), 아무도 자기와 보다 큰사람 없으면 1등
    for iii in result:
        if ii[0] < iii[0] and ii[1] < iii[1]:          # 키와, 몸무게가 모두 클경우에만 등수에 +1
            cnt += 1
    print(cnt, end=' ')

