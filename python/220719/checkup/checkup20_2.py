# divmod(x, y)는 x를 y로 나누고, 
# 결과를 tuple로 반환
# (몫, 나머지)

number = 123
result = 0

while number:
    number, remainder = divmod(number, 10)
    result += remainder

print(result)