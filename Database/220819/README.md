## 2022년 8월 19일(금)

> 데이터베이스! CASE, 서브쿼리



**수호아빠의 한줄평 : 오늘 과정은 어렵지 않고, 잘 이해가 된 듯!**



### CASE

- CASE문은 특정 상황에서 데이터를 변환하여 활용할 수 있음
- ELSE를 생략하는 경우 NULL값이 지정됨

```sqlite
CASE
	WHEN 조건식 THEN 식
	WHEN 조건식 THEN 식
	ELSE 식
END
```



### 서브쿼리

- 서브 쿼리는 특정한 값을 메인 쿼리에 반환하여 활용하는 것
- 실제 테이블에 없는 기준을 이용한 검색이 가능함
- 서브 쿼리는 소괄호로 감싸서 사용하며, 메인 쿼리의 칼럼을 모두 사용할 수 있음
- 메인 쿼리는 서브 쿼리의 칼럼을 이용할 수 없음
- 단일행 서브쿼리
  - 서브쿼리의 결과가 0 또는 1개인 경우
  - 단일행 비교 연산자와 함께 사용(=, <, <=, >=, >, <>)
- 다중행 서브쿼리
  - 서브쿼리 결과가 2개 이상인 경우
  - 다중행 비교 연산자와 함께 사용(IN, EXISTS 등)

```sqlite
-- users에서 평균 계좌 잔고가 높은 사람의 수는?
SELECT COUNT(*) 
FROM users
WHERE balance > (SELECT AVG(balance) FROM users)

-- 특정 성씨에서 가장 어린 사람들의 이름과 나이
SELECT
	last_name, 
	first_name,
	age
FROM users
WHERE (last_name, age) IN (
	SELECT last_name, MIN(age)
	FROM users
	GROUP BY last_name)
ORDER BY last_name;
```





