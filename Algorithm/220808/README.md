> ## 2022년 8월 08일(월)
>
> 알고리즘03 - 완전탐색 I (Exhaustive Search)



**수호아빠의 한줄평**

>  와..개념은 알 것 같았는데..문제 풀어보니까 아예 접근도 못했네..



#### 완전탐색 I (Exhaustive Search)



- 무식하게 다 해보기 (Brute-force)
  - 무식하게 밀어붙인다는 뜻
  - 가장 단순한 풀이기법
  - 단순 조건문과 반복문 이용한 풀이
  - 복잡한 알고리즘 보다, 아이디어를 어떻게 코드로 구현하는지 중요
- 델타 탐색 (Delta Search)
  - 상하좌우 탐색
  - 이차원 리스트의 인덱스(좌표)를 조작하여 상하좌우를 탐색
  - 이때의 변량을 델타(delta)값 이라고 함 (-1, +1 등등)

```python
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 상(x - 1, y)
nx = x + dx[0] 
ny = y + dy[0]

# 하(x + 1, y)
nx = x + dx[1]
ny = y + dy[1]

# 좌(x, y - 1)
nx = x + dx[2]
ny = y + dy[2]

# 우(x, y + 1)
nx = x + dx[3]
ny = y + dy[3]
```

