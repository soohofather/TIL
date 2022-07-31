## 2022년 7월 18일(월)

> 파이썬! 디버깅! 예러/예외 처리! 

#### "코드의 상태를 시중하게 출력해가며 심사숙고하는 것보다 효과적인 디버깅 도구는 없습니다."

#### 브라이언 커니핸, Unix for Beginners.

#### 1. 디버깅

- print 함수 활용
  
  - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각

- 개발 환경(text editor, IDE)등에서 제공하는 기능 활용
  
  - breakpoint, 변수 조회 등

- python tutor 활용 (단순 파이썬 코드인 경우)

- 뇌컴파일, 눈디버깅

#### 2. 에러와 예외

- 문법 에러(Syntax Error)
  
  - SyntaxError가 발생하면, 파이썬 프로그램은 실행이 되지 않음
  
  - 파일이름, 줄번호, ^ 문자를 통해 파이썬이 코드를 읽어 나갈 때(parser) 문제가
    발생한 위치를 표현
  
  - 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿(caret)기호(^)를 표시
  
  ```python
  File "<ipython-input-1-f8a097d0a685>", line 1 
  if else ^ 
  SyntaxError: invalid syntax
  ```
  
  - EOL (End of Line)
  
  ```python
  print('hello
  # File "<ipython-input-6-2a5f5c6b1414>", line 1
  # print('hello
  # ^
  # SyntaxError: EOL while scanning string literal
  ```
  
  - EOF (End of File)
  
  ```python
  print(
  # File "<ipython-input-4-424fbb3a34c5>", line 1
  # print(
  # ^
  # SyntaxError: unexpected EOF while parsing
  ```
  
  - Invalild syntax
  
  ```python
  while
  # File "<ipython-input-7-ae84bbebe3ce>", line 1
  # while
  # ^
  # SyntaxError: invalid syntax
  ```
  
  - assign to Iiteral
  
  ```python
  5 = 3
  # File "<ipython-input-28-9a762f2c796b>", line 
  1
  # 5 = 3
  # ^
  # SyntaxError: cannot assign to literal
  ```

```
- 예외(Exception)

- 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤

- 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러

- 실행 중에 감지되는 에러들을 예외(Exception)라고 부름

- 예외는 여러 타입(type)으로 나타나고, 타입이 메시지의 일부로 출력됨

- NameError, TypeError 등은 발생한 예외 타입의 종류(이름)

- 모든 내장 예외는 Exception Class를 상속받아 이뤄짐

- 사용자 정의 예외를 만들어 관리할 수 있음

- ZeroDivision : 0으로 나누고자 할 때 발생

- NameError : namespace 상에 정의 된 것이 없는 경우

- TypeError : 타입 불일치, int, str등

- TypeError - arguments 부족, 초과 : 2개를 넣어야 하는 곳에 1개나, 3개를 입력하게 되면 발생됨

- ValueError : 타입은 올바르나 그 안에 들어가는 값이 타입과 적절하지 않는 경우

- IndexError : 찾는 인덱스 값이 없는 경우

- KeyError

```python
song = {'IU': '좋은날'}
song['BTS']
# ------
# KeyError Traceback (most recent call last)
# 1 song = {'IU': '좋은날'}
# ----> 2 song['BTS']
# KeyError: 'BTS'
```

- ModuleNotFoundError : 존재하지 않는 모듈을 import 하는 경우

- ImportError : Module은 있으나 존재하지 않는 클래스/함수를 가져오는 경우

- IndentationError : Indentation이 적절하지 않는 경우
  
  ```python
  for i in range(3):
  print(i)
  # File "<ipython-input-56-78291925d94f>", line 2
  # print(i)
  # ^
  # IndentationError: expected an indented block
  ```

- KeyboardInterrupt – 임의로 프로그램을 종료하였을 때

#### 3. 예외 처리

- try 문(statement) / except 절(clause)을 이용하여 예외 처리 할 수 있음

- try문
  
  - 오류가 발생할 가능성이 있는 코드를 실행
  
  - 예외가 발생되지 않으면, except 없이 시랳ㅇ 종료

- except문
  
  - 예외가 발생하면, except 절이 실행
  
  - 예외 상황을 처리하는 코드를 받아서 적절한 조치를 ㅜ치함
  
  ```python
  try:
      num = input('숫자입력 :')
      print(int(num))
  except ValueError:
      print('숫자가 아닙니다')
  ```
  
  ```python
  try:
      num = input('100으로 나눌 값을 입력하시오: ')
      100/int(num)
  except (ValueError, ZeroDivisionError):
      print('제대로 입력해줘')
  ```
  
  ```python
  try:
      num = input('값을 입력하시오: ')
      100/int(num)
  except ValueError:
      print('숫자를 넣어주세요.')
  except ZeroDivisionError:
      print('0으로 나눌 수 없습니다.')
  except:
      print('에러는 모르지만 에러가 발생하였습니다.')
  ```

- 정리
  
  - try : 코드를 실행함
  
  - except : try문에서 예외가 발생 시 실행함
  
  - else : try 문에서 예외가 발새오디지 않으면 실행함
  
  - fanally : 예외 발생 여부와 관계 없이 항상 실행함

- 예시
  
  - 파일을 열고 읽는 코드를 작성하는 경우
    
    1. 파일 열기 시도
    
    2. 파일 없는 경우 ⇒ ‘해당 파일이 없습니다.’ 출력 (except)
    
    3. 파일 있는 경우 ⇒ 파일 내용을 출력 (else)
    
    4. 해당 파일 읽기 작업 종료 메시지 출력 (finally)
  
  ```py
  try: 
      f = open('nooofile.txt')
  except FileNotFoundError:
      print('해당 파일이 없습니다.')
  else:
      print('파일을 읽기 시작합니다.')
      print(f.read())
      print('파일을 모두 읽었습니다.')
      f.close()
  finally:
      print('파일 읽기를 종료합니다.')
  ```

#### 4. 예외 발생시키기

- raise를 통해 예외를 강제로 발생
  
  - raise <표현식> (메세지)
  
  - <표현식>에 예외타입지정 (주어지지 않을 경우 현재 스코프에서 활성화된 마지막 예외를 다시 일으킴)
  
  ```python
  raise
  # -------
  # RuntimeError Traceback (most recent call last)
  # ----> 1 raise
  # RuntimeError: No active exception to reraise
  ```
