
a = int(input())
b = int(input())
c = int(input())                # 한줄로 3번 들어오는 값을 a, b, c로 넣음

number = str(a * b * c)         # a b c 곱한 값을 하나하나로 나누기 위해 int에서 str로 타입 변경

for i in range(0,10):           # 0부터 9까지 숫자를 하나하나 찾을 첫번째 반복문
    cnt = 0                     # cnt를 0으로 설정
    for ii in number:           # number에서 처음부터 하나씩 순서대로 꺼내서 int로 바꾼뒤
        if i == int(ii):        # 그 꺼낸 숫자가 첫번째 반복문에서 내려온 0~9 숫자와 동일한 경우 cnt에 +1을함
            cnt += 1            
    print(cnt)
