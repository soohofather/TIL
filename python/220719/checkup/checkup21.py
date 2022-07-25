# print(int(str(number[::-1])))


a = int(input())
b = a
n = 0

while b != 0:
    b //= 10
    n += 1          # n = 자리수 찾기

o = 0
m = 10 ** (n - 1)   # m = 위에서 찾은 자릿수로 나누기 시작
while a > 0:
    b = a % 10
    o += b * m
    a //= 10
    m //= 10
    
print(o)