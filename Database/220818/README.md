## 2022년 8월 18일(목)

> 데이터베이스! 기본함수와 연산, GROUP BY, ALTER TABLE



**수호아빠의 한줄평 : 쬐끔씩 범위가 넓어져가며.. 어렵지는 않지만 엄청 넓은 느낌..?**



### 기본 함수와 연산

- 문자열 함수

  - SUBSTR(문자열, start, length) : 문자열 자르기

    - 시작 인덱스는 1, 마지막 인덱스는 -1

  - TRIM(문자열), LTRIM(문자열), RTRIM(문자열) : 문자열 공백 제거

  - LENGTH(문자열) : 문자열 길이

    ```sqlite
    -- 문자열 길이 LENGTH
    SELECT 
        LENGTH(first_name),
        first_name
    FROM users
    LIMIT 5;
    -- LENGTH(first_name)  first_name
    -- ------------------  ----------
    -- 2                   정호
    -- 2                   경희
    -- 2                   정자
    -- 2                   미경
    -- 2                   영환

  - REPLACE(문자열, 패턴, 변경값) : 패턴에 일치하는 부분을 변경

    ```sqlite
    -- 문자열 변경 REPLACE
    -- 016-7280-2855 => 01672802855
    SELECT 
        first_name,
        phone,
        REPLACE(phone, '-', '')
    FROM users
    LIMIT 5;
    ```

  - UPPER(문자열), LOWER(문자열) : 대소문자 변경

  - || : 문자열 합치기(concatenation)

    ```sqlite
    -- pipe sign 엔터 위에 있어요 보통
    -- 문자열 합치기 ||
    -- (성+이름) 출력, 5명만
    SELECT 
        last_name || first_name 이름,
        age,
        country,
        phone,
        balance
    FROM users
    LIMIT 5;
    
    -- 이름   age  country  phone          balance
    -- ---  ---  -------  -------------  -------
    -- 유정호  40   전라북도     016-7280-2855  370
    -- 이경희  36   경상남도     011-9854-5133  5900
    -- 구정자  37   전라남도     011-4177-8170  3100
    -- 장미경  40   충청남도     011-9079-4419  250000
    -- 차영환  30   충청북도     011-2921-4284  220
    ```

- 숫자 함수

  - ABS(숫자) : 절대 값

  - SIGN(숫자) : 부호 (양수 1, 음수 -1, 0 0)

  - MOD(숫자1, 숫자2) : 숫자1을 숫자2로 나눈 나머지

    ```sqlite
    -- 숫자 활용
    SELECT MOD(5, 2)
    FROM users
    LIMIT 1;
    ```

  - CEIL(숫자), FLOOR(숫자), ROUND(숫자, 자리) : 올림, 내림, 반올림

    ```sqlite
    -- 올림, 내림, 반올림
    SELECT CEIL(3.14), FLOOR(3.14), ROUND(3.14)
    FROM users
    LIMIT 1;
    ```

  - POWER(숫자1, 숫자2) : 숫자1의 숫자2 제곱

    ```sqlite
    -- 9^2
    SELECT POWER(9, 2)
    FROM users
    LIMIT 1;
    ```

  - SQRT(숫자) : 제곱근

    ```sqlite
    -- 9의 제곱근
    SELECT SQRT(9)
    FROM users
    LIMIT 1;
    ```

- 산술 연산자

  - +, -, *, /와 같은 산술 연산자와 우선 순위를 지정하는 () 기호를 연산에 활용할 수 있음



### GROUP BY

- SELECT 문의 optional 절

- 행 집합에서 요약 행 집합을 만듦

- 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듦

- **문장에 WHERE 절이 포함된 경우 반드시 WHERE 절 뒤에 작성해야 함**

- GROUP BY절에 명시하지 않은 컬럼은 별도로 지정할 수 없음

  - 그룹마다 하나의 행을 출력하게 되므로 집계 함수 등을 활용해야 함

- GROUP BY의 결과는 정렬되지 않음

  - 기존의 순서와 바뀌는 모습도 있음
  - 원칙적으로 관계형 데이터베이스에서는 ORDER BY를 통해 정렬

- **HAVING**

  - 집계함수는 WHERE 절의 조건식에서는 사용할 수 없음(실행 순서에 의해)

    - WHERE로 처리하는 것이 GROUP BY 그룹화보다 순서상 앞서 있기 때문

  - 집계 결과에서 조건에 맞는 값을 따로 활용하기 위해서 HAVING을 활용

    ```sqlite
    -- GROUP BY WHERE를 쓰고 싶다.
    -- 100번 이상 등장한 성만 출력하고 싶음. 
    SELECT last_name, COUNT(last_name)
    FROM users
    WHERE COUNT(last_name) > 100
    GROUP BY last_name;
    -- 오류 발생!
    -- Parse error: misuse of aggregate: COUNT()
    --   LECT last_name, COUNT(last_name) FROM users WHERE COUNT(last_name) > 100 GROUP
    
    -- 조건에 따른 GROUP 하시려면
    -- HAVING을 쓴다!
    SELECT last_name, COUNT(last_name)
    FROM users
    GROUP BY last_name
    HAVING COUNT(last_name) > 100;
    ```

- SELECT 문장 실행 순서

  - FROM => WHERE => GROUP BY => HAVING => SELECT => ORDER BY
    1. FROM 테이블을 대상으로
    2. WHERE 제약조건에 맞춰서 뽑아서
    3. GROUP BY 그룹화한다.
    4. HAVING 그룹 중에 조건과 맞는 것 만을
    5. SELECT 조회하여
    6. ORDER BY 정렬하고
    7. LIMIT/OFFSET 특정 위치의 값을 가져온다.

  

### ALTER TABLE

- 테이블 이름 변경
  - **ALTER TABLE** 테이블 이름 **RENAME TO** 새로운 테이블 이름;
- 새로운 column 추가
  - **ALTER TABLE** 테이블 이름 **ADD COLUMN** 추가할 컬럼 이름;
- column 이름 수정 (new in sqlite 3.25.0)
  - **ALTER TABLE** 테이블 이름 **RENAME COLUMN** 지금 컬럼 이름 **TO** 새로운 컬럼 이름;
- column 삭제 (new in sqlite 3.35.0)
  - **ALTER TABLE** 테이블 이름 **DROP COLUMN** 컬럼 이름;

```sqlite
-- 새로운 컬럼 이름은 created_at 이며, TEXT 타입에 NULL 설정!
ALTHER TABLE news ADD COLUMN created_at TEXT NOT NULL;

-- 실패
Error: Cannot add a NOT NULL column with default value NULL

-- 새로 추가하려는 컬럼의 디폴트를 NOT NULL로 설정하여 추가하려는데, 
-- 막 추가된 컬럼의 값은 NULL이라 충돌

-- 1번 해결방법은 NULL 세팅 없이 컬럼 추가
-- 2번 해결방법은 기본 값을 설정하여 컬럼 추가

ALTHER TABLE news ADD COLUMN created_at TEXT NOT NULL DEFAULT '소제목';
```

