
a, b = input().split()      # 두 숫자를 a, b로 넣음

a = int(a[::-1])
b = int(b[::-1])            # 각 숫자를 거꾸로 한 뒤 int로 타입변경

print(a if a > b else b)    # a > b면 a를, 아니면 b를 출력