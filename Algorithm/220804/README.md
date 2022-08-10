> ## 2022년 8월 04일(목)
>
> 알고리즘02 - 이차원리스트의 순회



**수호아빠의 한줄평**

>  어렵다...........더 다양한 사고가 필요한 느낌..



- 순회

```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]

# 이중 for문을 이용한 행 우선 순회
for i in range(3):
    for j in range(4):
        print(matrix[i][j], end=' ')
   	print()								# 1 2 3 4
        								# 5 6 7 8
            							# 9 0 1 2
                
# 이중 for문을 이용한 열 우선 순회
for i in range(4):
    for j in range(3):
        print(matrix[j][i], end=' ')
        print()							# 1 5 9
        								# 2 6 0
            							# 3 7 1
                						# 4 8 2
```

- 순회를 이용한 총합

```python
matrix = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]

# 순회
for i in range(3):
    for j in range(4):
        total += matrix[i][j]
print(total)						# 12

# 파이써닉
total = sum(map(sum, matrix))

print(total)						# 12
```

- 순회를 이용한 두 행열 곱

```python
# 3 6 9
# 8 5 2
# 9 8 7
# 6 5 4 

list_a = [list(map(int, input().split())) for i in range(2)]
list_b = [list(map(int, input().split())) for i in range(2)]
list_c = [[0] * 3 for _ in range(2)]

for i in range(2):
    for j in range(3):
        list_c[i][j] = list_a[i][j] * list_b[i][j]

for i in range(2):
    for j in range(3):
        print(list_c[i][j], end=' ')
    print()
```

- 순회를 이용한 행렬의 최대값, 최소값

```python
# 최대값

matrix = [
    [0, 5, 3, 1]
    [4, 6, 10, 8]
    [9, -1, 1, 5]
]

max_value = 0

for i in range(3):
    for j in range(4):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            
print(max_value)		# 10

# 최소값

min_value = 9999999999

for i in range(3):
    for j in range(4):
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
            
print(min_value)		# -1
```



