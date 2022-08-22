## 2022년 8월 22일(월)

> 데이터베이스! JOIN



**수호아빠의 한줄평 : 어렵지 않게 이해는 되었다, 다만 이너조인과 아웃터조인의 미묘한 차이를 정확히 이해했는지를 스스로 알아봐야할듯**



### JOIN

- **관계형 데이터베이스의 가장 큰 장점이자 핵심적인 기능**
- 일반적으로 데이터베이스에는 하나의 테이블에 많은 데이터를 저장하는 것이 아니라 여러 테이블로 나눠 저장하게 되며, 여러 테이블을 결합(Join)하여 출력하여 활용
- 일반적으로 레코드는 기본키(PRIMARY KEY)나 외래키(FOREIGN KEY) 값의 관계에 의해 결합함
- INNER JOIN : 두 테이블에 모두 일치하는 행만 반환

```sqlite
-- A와 B테이블에서 값이 일치하는 것들만 
SELECT *
FROM users INNER JOIN role
    ON users.role_id = role.id;
    
-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 1   관리자   1        1   admin
-- 2   김철수   2        2   staff
-- 3   이영희   2        2   staff
```

- OUTER JOIN : 동일한 값이 없는 행도 반환
  - LEFT OUTER, RIGHT OUTER, FULL OUTER

```sqlite
-- LEFT OUTER JOIN
SELECT * 
FROM articles LEFT OUTER JOIN users
    ON articles.user_id = users.id;

-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1
-- 2   2번글    222      2        2   김철수   2
-- 3   3번글    333      1        1   관리자   1
-- 4   4번글    444

-- FULL OUTER JOIN
SELECT * 
FROM articles FULL OUTER JOIN users
    ON articles.user_id = users.id;
-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1
-- 2   2번글    222      2        2   김철수   2
-- 3   3번글    333      1        1   관리자   1
-- 4   4번글    444
--                              3   이영희   2
```

-  CROSS JOIN : 모든 데이터의 조합

```sqlite
-- CROSS JOIN
SELECT * 
FROM users CROSS JOIN role;
-- id  name  role_id  id  title
-- --  ----  -------  --  -------
-- 1   관리자   1        1   admin
-- 1   관리자   1        2   staff
-- 1   관리자   1        3   student
-- 2   김철수   2        1   admin
-- 2   김철수   2        2   staff
-- 2   김철수   2        3   student
-- 3   이영희   2        1   admin
-- 3   이영희   2        2   staff
-- 3   이영희   2        3   student
```

- 3개 테이블 JOIN

```sqlite
-- 3개 테이블 조인
SELECT * 
FROM articles
    JOIN users
        ON articles.user_id = users.id
    JOIN role
        ON users.role_id = role.id;
-- id  title  content  user_id  id  name  role_id  id  title
-- --  -----  -------  -------  --  ----  -------  --  -----
-- 1   1번글    111      1        1   관리자   1        1   admin
-- 2   2번글    222      2        2   김철수   2        2   staff
-- 3   3번글    333      1        1   관리자   1        1   admin
```

