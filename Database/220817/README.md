## 2022년 8월 17일(수)

> 데이터베이스! CRUD, WHERE, LIKE, ORDER BY



**수호아빠의 한줄평 : 어제는 좀 해멨는데.. 오늘은  조금 개념을 잡은 듯 하다.**



### CRUD

- CREATE
  - INSERT INTO 테이블 이름 VALUES 값
    - 값을 테이블에 맞게 넣는 경우
  - INSERT INTO 테이블 이름 (컬럼1, 컬럼2) VALUES  (값1, 값2)
    - 원하는 컬럼에만 값 넣는 경우
- READ
  - SELECT * FROM 테이블이름
    - ORDER BY, DISTINCT, WHERE , LIMIT, GROUP BY 등등 함께 사용
- UPDATE
  - UPDATE 테이블이름 SET 컬럼1=값1 , 컬럼2=값2 WHERE rowid=값;
    - rowid 기준에 있는 컬럼에 값을 넣음
- DELETE
  - DELETE FROM 테이블이름 WHERE rowid=값;
    - 해당 rowid 삭제됨
    - 다음 생성시 rowid 값 다음것부터 진행



### WHERE

- 특정 조건으로 데이터 조회하기

```sqlite
SELECT * FROM 테이블이름 WHERE 조건;
```

- WHERE절에서 사용할 수 있는 연산자
  - 비교 연산자
    -  =, >, >=, <, <= 는 숫자 혹은 문자 값의 대/소, 동일 여부를 확인하는 연산자
  - 논리 연산자
    - AND : 앞에 있는 조건과 뒤에 오는 조건이 모두 참인 경우
    - OR : 앞의 조건이나 뒤의 조건이 참인 경우
    - NOT : 뒤에 오는 조건의 결과를 반대로

```sqlite
-- 주의!

-- 1. 키가 175이거나, 키가 183이면서 몸무게가 80인 사람
WHERE HEIGHT = 175 OR HEIGHT = 183 AND WEIGHT = 80
-- 2. 키가 175 또는 183인 사람 중에서 몸무게가 80인 사람
WHERE (HEIGHT = 175 OR HEIGHT = 183) AND WEIGHT = 80

-- 1번은 키가 175이고, 몸무게는 80이 아니어도 되는 사람 + 키가 183이면서 몸무게가 80인사람
-- 2번은 키가 175나 183이면서, 몸무게가 80인사람
```

- SQL 사용할 수 있는 연산자
  - BETWEEN 값1 AND 값2
    - 값1과 값2 사이의 비교 (값1 <= 비교값 <= 값2)
  - IN (값1, 값2, …)
    - 목록 중에 값이 하나라도 일치하면 성공
  - LIKE
    - 비교 문자열과 형태 일치
    - 와일드카드 (% : 0개 이상 문자, _ : 1개 단일 문자)
  - IS NULL / IS NOT NULL
    - NULL 여부를 확인할 때는 항상 = 대신에 IS를 활용
  - 부정 연산자
    - 같지 않다. (!=, ^=, <>) 
    - ~와 같지 않다. (NOT 칼럼명 =)
    - ~보다 크지 않다. (NOT 칼럼명 >)

- 연산자 우선순위
  1. 괄호 ()
  2. NOT
  3. 비교 연산자, SQL
  4. AND
  5. OR



### Aggregate function

- 집계함수
  - 값 집합에 대한 계산을 수행하고 단일 값을 반환
  - 여러 행으로부터 하나의 결괏값을 반환하는 함수
  - SELECT 구문에서만 사용됨
  - COUNT
    - 그룹의 항목 수를 가져옴
  - AVG
    - 모든 값의 평균을 계산
  - MAX
    - 그룹에 있는 모든 값의 최대값을 가져옴
  - MIN
    - 그룹에 있는 모든 값의 최소값을 가져옴
  - SUM
    - 모든 값의 합을 계산



### LIKE

- 패턴 일치를 기반으로 데이터를 조회하는 방법
- SQLite는 패턴 구성을 위한 2개의 wildcards를 제공
  - % (percent sign) : 0개 이상의 문자
    - 이 자리에 문자열이 있을 수도, 없을 수도 있다.
  - _ (underscore) : 임의의 단일 문자
    - 반드시 이 자리에 한 개의 문자가 존재해야 한다.
  - 2% : 2로시작하는 값
  - %2 : 2로 끝나는 값
  - %2% : 2가 들어가는 값
  - _2% : 아무 값이 하나 있고 두 번째가 2로 시작하는 값
  - 1___ : 1로 시작하는 총 4자리 인 값
  - 2\_%\_% / 2__% : 2로 시작하고 적어도 3자리인 값



### ORDER BY

- 조회 결과 집합을 정렬
- SELECT 문에 추가하여 사용
- 정렬 순서를 위한 2개의 keyword 제공
  - ASC – 오름차순 (default)
  - DESC - 내림차순

```sqlite
-- 오름차순 (default)
SELECT * FROM 테이블이름 ORDER BY 컬럼 ASC;

-- 내림차순
SELECT * FROM 테이블이름 ORDER BY 컬럼 DESC;
```

