number = int(input())
result = 0                        

for i in range(number):               # 0부터 넣은 숫자까지 순회할 반복문 
  il_list = list(map(int, str(i)))    # i의 숫자를 str으로 만들어서 각 자리숫자를 다시 숫자로 만들어서 리스트를 만듬. 1 = [1], 23 = [2,3], 234 = [2, 3, 4]
  result = i + sum(il_list)           # result는 지금 내려온 숫자에 그 숫자의 자릿수들의 합
  if result == number:                # result가 처음 넣은 숫자와 같으면 브레이크. 
    print(i)                          
    break
else:
  print(0)

