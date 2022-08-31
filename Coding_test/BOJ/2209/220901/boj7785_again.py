# pypy로 성공, python3는 시간초과

TC = int(input())

log = {}

for _ in range(TC):
    name, inout = input().split()
    if inout == 'enter':
        log[name] = 1
    else:
        log[name] -= 1

person_in = []

for i in log:
    if log[i] == 1:
        person_in.append(i)
person_in.sort(reverse = True)

for ii in person_in:
    print(ii)