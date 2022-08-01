## 2022년 7월 28일(목)

> 알고리즘! 자료구조04 - 딕셔너리(Dictionary)



**수호아빠의 한줄평**

>  딕셔너리는 잘쓰면 좋다는 것은 알겠는데..뭔가 익숙하지가 않네..



### 딕셔너리 (dictionary)



- 파이썬에는 딕셔너리(dict) 자료구조가 내장 되어있다.
- 딕셔너리는 Key 와 Key-Value로 구성되어있다.
  - 해시 테이블(Hash Table)을 이용하여 Key: value 저장
- 딕셔너리는 **연산속도가 리스트보다 빠르다.**
- 기본 문법

```python
a = {
    'name': 'kyle'
    'gender': 'male'
    'address': 'seoul'
}

# 삽입
a['job'] = 'coach' 

# 수정
a['name']: 'justin'

# 삭제 및 반환
gender = a.pop('gender')	# a를 출력하면 gender가 빠져있고,
							# gender를 출력하면 gender의 value인 male이 나옴
    						# 없는 key값을 넣으면 에러 발생
        
phone = a.pop('phone', '010-0000-0000')	# a를 출력하면 아무 변화 없음
                                        # phone을 출력하면 phone의 value인 
                                        # 010-0000-0000 출력
        
# 조회
print(a['name'])				# kyle, 없는 key 조회시 에러
print(a.get('name'))			# kyle
print(a. get('phone', '없음'))   # 없음
```

- 딕셔너리 메서드

  - .Keys() : 딕셔너리의 key 목록이 담긴 dict_keys 객체 반환

  ```python
  a = {
      'name': 'kyle'
      'gender': 'male'
      'address': 'seoul'
  }
  
  print(a.keys()) 		# dict_keys(['name', 'gender', 'address'])
  
  for key in a.keys():
      print(key)			# name
      					# gender
          				# address
              
  for key in a:
      print(key)			# name
      					# gender
          				# address
  ```

  - .values()

  ```python
  a = {
      'name': 'kyle'
      'gender': 'male'
      'address': 'seoul'
  }
  
  print(a.values())		# dict_valuse(['kyle', 'male', 'seoul'])
  
  for value in a.values():
      print(value)		# kyle
      					# male
          				# seoul
  ```

  - items()

  ```python
  a = {
      'name': 'kyle'
      'gender': 'male'
      'address': 'seoul'
  }
  
  print(a.times())
  # dict_iteams([('name', 'kyle'), ('gender', 'male'), ('address', 'seoul')])
  
  for item in a.items():
      print(item)			# ('name', 'kyle')
      					# ('gender', 'male')
          				# ('address', 'seoul')
  
  for key, value in a.items():
      print(key value)	# name kyle
      					# gender male
          				# address seoul
  ```

  
