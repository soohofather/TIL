## 2022년 7월 21일(목)

> 파이썬! 응용 및 모듈 심화 그리고 가상환경



**수호아빠의 한줄평 : 조금 더 간결한 코딩을 가능하게 하는 파트?**



#### 1. 추가문법



- List Comprehension : 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법

```python
<expression> for <변수> in <iterable>
<expression> for <변수> in <iterable> if <조건식>

# 1~3의 세제곱의 결과가 담긴 리스트를 만드시오.

# 일반
cubic_list = []
for number in rage(1, 4):
    cubic_list.append(number**3)
print(cubic_list)

# List comprehension
[number**3 for number in rage(1,4)] # 특정한 요소들로 구성된 리스트 만들 떄
```

- Dictionary Comprehension

```python
# 일반
cubic_dict = {}
for number in rage(1,4):
    cubic_dict[number] = number ** 3
print(cubic_dict)

# Dictionary Comprehension
{number: number**3 for number in ranger(1,4)}
```

- Lambda [parameter]
  - 람다함수 
    - 표현식을 계산한 결과값을 반환하는 함수, 이름이 없는 함수라 익명함수로 불림
  - 특징
    - return문을 가질 수 없음
    - 간편 조건문 외 조건문이나 반복문을 가질 수 없음
  - 장점
    - 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
    - def를 사용할 수 없는 곳에서도 사용가능
- filter(function, iterable)
  - 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)적용하고, 그 결과가 True인 것들을 filter object로 반환

```python
# 일반
result = []
for number in numbers:
    if number % 3 == 0:
        result.append(number)
print(result)

# Lambda, filter
print(list(filter(lambda n: n%3 == 0, numbers)))
```



#### 2. 모듈 심화



- 파이썬 표준 라이브러리
  - 파이썬에 기본적으로 설치된 모듈과 내장 함수
    - [https://docs.python.org/ko/3/library/index.html](https://docs.python.org/ko/3/library/index.html)

- 파이썬 패키지 관리자(pip)

  - PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템
  - 패키지 설치
    - 최신버전 / 특정버전 / 최소버전을 명시하여 설치 할 수 있음
    - 이미 설치 되어있는 경우 이미 설치되어있음을 알리고 아무것도 하지 않음

  ```python
  $ pip install SomPackage
  $ pip install SomePackage==1.0.5
  $ pip install 'SomePacage>=1.0.4'
  
  # 모두 bash, cmd 환경에서 사용되는 명령어
  ```

  - 패키지 삭제

  ```python
  $ pip uninstall SomePackage
  ```

  - 패키지 활용 명령어

  ```python
  $ pip list				# 패키지 목록
  
  $ pip SomePackage		# 패키지 정보
  
  $ pip freeze			# 설치된 패키지를 pip intall에서 활용하는 형식으로 출력
  						# 및 해당하는 목록을 requrements.txt로 만들어 관리
  
  $ pip freeze > requirements.txt  	# 패키지 목록을 설치  
  $ pip install -r requirements.txt	# 패키지 목록을 삭제
  ```

  

#### 3. 가상환경



- 여러 프로젝트 진행시 각 프로젝트의 버전이 상이할 수 있음. 이 때, 가상환경을 만드렁 프로젝트 별로 독립적인 패키지를 관리할 수 있음

- venv

  - 가상 환경을 만들고 관리하는데 사용되는 모듈 (Python 버전 3.5부터)
  - 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음.
    - 실행에서 가상환경을 활성화 시켜 해당 폴더에 있는 패키지를 관리/사용
  - 가상화경 생성

  ```python
  $ python -m venv <폴더명>
  ```

  - 가상환경 활성화 / 비활성화

  ```python
  # cmd.exe
  # <venv>는 가상환경을 포함한 디렉토리의 이름
  
  c:/> <venv>\Scripts\activate.bat
  
  # PowerShell
  PS c:/> <venv>\Scripts\Activate.ps1
  
  #비활성화
  
  $ deactivate
  ```
