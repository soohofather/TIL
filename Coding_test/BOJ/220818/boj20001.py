import sys

sys.stdin = open('test.txt', 'r', encoding='UTF-8')

start = input()
status = []

while True:
    duck = input()
    if duck == '고무오리 디버깅 끝':
        break
    elif duck == '문제':
        status.append(duck)
    else:
        if len(status) == 0:
            status.append(duck)
            status.append(duck)
        else:
            status.pop()
print('고무오리야 사랑해' if len(status) == 0 else '힝구')