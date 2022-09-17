import sys

sys.stdin = open('test.txt')

TC = int(input())

cards = []

for _ in range(TC):
    cards.append(list(map(int, input().split())))


for numbers in cards:
    cnt = 0
    result = 0  
    for i in range(3):
        for ii in range(TC):
            if numbers[i] == cards[ii][i]:
                cnt += 1
        else:
            if cnt == 1:
                cnt = 0
                result += numbers[i]
            else:
                cnt = 0
    print(result)
    result = 0