N = input()

if len(N) == 1:
    N = '0' + N

first_number = N
second_number = ''
cnt = 0

while True :

    cnt += 1

    second_number = str(int(N[0]) + int(N[1]))

    if len(second_number) == 1:
        second_number = '0' + second_number

    N = N[1] + second_number[1]
    
    if N == first_number:
        break
print(cnt)