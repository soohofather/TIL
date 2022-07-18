# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# 양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

# input : 123


n = int(input('양의 정수를 입력해주세요: '))
m = 10
jarisu = 1

for mm in range(n):
    if n < m:
        break
    elif n > 0:
        jarisu += 1
        m *= 10
print(jarisu)
