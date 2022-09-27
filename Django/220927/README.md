# 2022년 9월 27일 (화)

> Django04!  실습문제 풀이



`수호아빠의 한마디: 와.. ORM 아예 생각도 안나네..큰일이다..`



# 실습 문제

1. 아래 내용의 데이터 추가하기.
   - content : 실습 제출
   - priority : 5
   - deadline : 2022-09-27

```python
Todo.objects.create(content = '실습 제출', priority = 5, deadline = '2022-09-27')
```

2. 모든 데이터를 id를 기준으로 오름차순으로 정렬해서 가져오기.

```python
Todos = Todo.objects.order_by('id')
```

3. 모든 데이터를 deadline을 기준으로 내림차순으로 정렬해서 가져오기.

```python
todos = Todo.objects.order_by('-deadline')
```

4. 모든 데이터를 priority가 높은 순으로 정렬해서 가져오기.

```python
todos = Todo.objects.order_by('-priority')
```

5. priority가 5인 모든 데이터를 id를 기준으로 오름차순으로 정렬해서 가져오기.

```python
todos = Todo.objects.filter(priority=5).order_by('id') 
```

6. completed가 True인 모든 데이터를 id를 기준으로 오름차순으로 정렬해서 가져오기.

```python
todos = Todo.objects.filter(completed=True).order_by('id')
```

7. priority가 5인 데이터의 개수

```python
count = Todo.objects.filter(priority=5).count()
```

8. id가 1인 데이터 1개 가져오기.

```python
count = Todo.objects.get(id=1)
```

9. id가 1인 데이터 삭제하기.

```python
count = Todo.objects.get(id=1)

count.delete()
```

10. id가 10인 데이터의 priority 값을 5로 변경하기.

```python
todo = Todo.objects.get(id=10)

todo.priority = 5

todo.save()
```
