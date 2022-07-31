# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

# 평가 기준
# 점수 범위 : 평가
#  90 ~ 100 : A
#  70 ~   89 : B
#  40 ~   69 : C
#    0 ~   39 : D
# 로 평가되어야 한다.

n = int(input())

if n < 40:
    print('D')
elif n < 70:
    print('C')
elif n < 90:
    print('B')
else:
    print('A')
    
