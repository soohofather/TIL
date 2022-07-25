## 2022년 7월 12일(화)

> 파이썬! 조건문과 반복문 (if, elif, else, while, for in)



### 제어문

- 특정 상황에 따라 코드를 선택적으로 실행하거나, 계속 실행하는 제어가 필요할 때
- 제어문은 순서도(flow chart)로 표현이 가능



#### 1. 조건문

- 조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용

- expression에는 참/거짓에 대한 조건식

  ```python
  if < expression >:
      # Run this cold block
  else : 
      # Run this code block
      
  # 조건이 참인 경우 이후 들여쓰기 되어있는 코드 블럭 실행
  # 이외의 경우 else 이후 들여쓰기 되어있는 코드 블럭 실행
  # else는 선택적으로 활용 가능
  ```



#### 2. 복수조건문

```python
if <expression>:
    # code block
elif <expression>:
    # code block
elif <expression>:
    # code block
else:
    # code block
```



#### 3. 중첩조건문

- 조건문은 다른 조건문에 중첩되어 사용될 수 있음

- 들여쓰기를 유의하여 작성할 것

  ```python
  dust = 80
  
  if dust > 150:
      print('매우나쁨')
      if dust > 300;					# 중첩조건문 부분 (150이면 매우나쁨만, 300이상이면 매우나쁨 + 실외활동을 자제하세요)
      	print('실외 활동을 자제하세요.') 
  if dust > 80:
      print('나쁨')
  if dust > 30:
      print('보통')
  else:
      print('좋음')
  print('미세먼지 확인 완료')
  ```

  

#### 4. 조건표현식

- 조건표현식을 일반적으로 조건에 따라 값을 할당할 때 활용

  ```python
  `<true인 경우 값> if <expression> else <false 인 경우의 값>`
  
  $ value = num if num >= 0 else -num
  
  # value 참일 경우
  # if num 위 value가 참인 <expression>
  # else 위 value가 거짓인 경우
  ```

  

#### 5. 반복문

- 특정 조건을 도달할 때까지, 계속 반복되는 일련의 문장

- while 문 (종료조건에 해당하는 코드를 통해 반복문을 종료시켜야함)

  ```python
  a = 0
  while a < 5:	# 종료조건, 없으면 a가 무한대로 증가함
      print(a)	 
      a += 1		 
  print('끝')
  ```

  ```python
  n = 0
  total = 0
  user_input = int(input()) # 값 초기화
  
  while n <= user_input:    # 종료조건, 사용자가 넣은 숫자까지만 작업
      total += n
      n += 1
  print(total)
  ```

- for 문 (반복가능한 객체를 모두 순회하면 종료, 별도의 종료조건이 필요 없음)

  - 순회 할 수 있는 자료형(str,list,dict 등), 순회형 함수(range,enumerate)
  - 문자열 순회

  ```python
  for <변수명> in <iterable>: # 기본적인 for문 
      # code block
  ```

  ```python
  for fruit in ['apple', 'mango', 'banana']: # 과일 3개 순차적으로 나오고 끝 출력
  	print(fruit)
  print('끝')
  ```

  ```python
  chars = input()
  
  for char in chars: # 입력한 값이 하나씩 하나씩 출력됨 => 가로로 입력된 것이 세로로 하나씩 나옴
      print(char)
  ```

  ```python
  chars = input()
  
  for idx in range(len(chars)):
      print(chars[idx])
  ```

  - enumerate 순회

  ``` python
  members = ['민수', '영희', '철수']
  
  for in rage(len(members)):
      print(f'{i} {members[i]})
  ```

  ```py
  members = ['민수', '영희', '철수']
  
  for i, member in enumerate(members):
  	print(i, member)
  ```

  ```python
  members = ['민수', '영희', '철수']
  
  enumerate(members) # <enumerate at 0x105d3e100>
  
  list(enumerate(members)) # [(0, '민수'), (1, '영희'), (2, '철수')] <- 숫자와 값의 tuple
  
  list(enumerate(members, start=1)) # [(1, '민수'), (2, '영희'), (3, '철수')] # start를 지정하면 그 값부터 시작
  ```

  - 딕셔너리 순회

  ```python
  grades = {'john':80, 'eric':90}	#딕셔너리는 기본적으로 key를 순회하며, key를 통해 값을 활용
  for name in grades:
      print(name)					
  
  # john
  # eric
  ```

  ```python
  grades = {'john':80, 'eric':90}
  for name in grades:
      print(name, grades[name])
      
  # john 80
  # eric 90 
  ```

- 제어

  - break (반복문을 종료)

  ```python
  n = 0
  while Ture:
      if n == 3:
          break   # n = 3일때, break를 만나서 아래로 내려가지 않고 바로 종료됨
      print(n)
      n += 1
      
  # 0
  # 1
  # 2
  ```

  ```python
  for i in range(10):
      if i > 1:
          print('0과 1만 필요해!')
          break
      print(i)
      
  # 0
  # 1
  # 0과 1만 필요해!
  ```

  - continue (continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행)

  ```python
  for i in range(6):
      if i % 2 == 0: 
          continue		# continue를 만나면, 이후 코드인 print(i)가 실행되지 않고 바로 다음 반복을 실행
      print(i)			# 0,2,4는 나머지가 0이기때문에 continue를 만남
      
  # 1
  # 3
  # 5
  ```

  - for-else (끝까지 반복문을 실행한 이후에 else문 실행. 단, break를 통해 중간에 종료되는 경우 else 문은 실행되지 않음)

  ```python
  for char in 'apple':
      if char == 'b':
          print('b!')
          break
  else:
      print('b가 없습니다.')	# break에 걸리지 않아서 else까지 내려옴
      
  # b가 없습니다.
  ```

  ```python
  for char in 'banana':
      if char == 'b':
          print('b!')
          break
  else:
      print('b가 없습니다.') # 첫번째 b에서 break에 걸려서 b!하고 끝
      
  # b!
  ```

  
