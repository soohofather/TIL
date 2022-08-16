## 2022년 8월 16일(화)

> 데이터베이스 첫시간! 데이터 베이스 기초!



**수호아빠의 한줄평 : 오늘 기초만 배우긴했는데.. 첫 이미지는 일단 괜찬다! 싶다.**



### 데이터베이스

- 체계화된 데이터 모임
- 여러사람이 공유하고 사용할 목적으로 통합관리 되는 정보의 집합
- 내용을 고도로 구조화함으로써 검색과 갱신의 효율화
- 데이터베이스로 얻는 장점들
  - 데이터 중복 최소화
  - 데이터 무결성 (정확한 정보를 보장)
  - 데이터 일관성
  - 데이터 독립성 (물리적 / 논리적)
  - 데이터 표준화
  - 데이터 보안 유지



### RDB

- 관계형 데이터베이스(RDB, Realational Database)
  - 키와 값들의 간단한 관계를 표형태로 정리한 데이터베이스
- 스키마, 테이블
  - 스키마 : 자료의 구조, 표현방법, 관계등 전반적인 명세를 기술한 것
  - 테이블 : 열(컬럼/필드)과 행(레코드/값)을 사용해 조직된 데이터 요소들의 집합

```sqlite
-- 테이블 만들기

CREATE TABLE healthcare (
id PRIMARY KEY,
sido INTEGER NOT NULL,
gender INTEGER NOT NULL,
age INTEGER NOT NULL,
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,
va_left REAL NOT NULL,
va_right REAL NOT NULL,
blood_pressure INTEGER NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);

-- 각 열마다 PRIMARY KEY, NOT NULL로 스키마를 만들고 테이블을 만듬

-- csv import 하기
.mode csv 
.import health.csv healthcare

-- health.csv 파일의 데이터를 방금 만든 테이블에 넣음
```



### RDBMS

- 관계형 데이터베이스 관리 시스템 (RDBMS)
  - MySQL, SQLite, PostgreSQL, ORACLE, SQL Server 등등



### SQLite

- 파일 형식으로 사용하는 비교적 가벼운 데이터베이스

- 구글 안드로이드에 기본적으로 탑재된 데이터베이스

- 임베디드 소프트웨어에도 많이 활용

- 로컬에서도 간단히 DB구성 가능

- 오픈소스라 자유롭게 사용가능

- SQLite Data Type

  1. NULL
  2. INTEGER
     - 크기에 따라 0, 1, 2, 3, 4, 6 또는 8바이트에 저장된 부호 있는 정수
  3. REAL
     - 8바이트 부동 소수점 숫자로 저장된 부동 소수점 값
  4. TEXT
  5. BLOB 
     - 입력된 그대로 정확히 저장된 데이터 (별다른 타입 없이 그대로 저장)

- Sqlite Type Affinity (1/2)

  - 특정 컬럼에 저장하도록 권장하는 데이터 타입

  1. INTEGER
     - INT
     - INTEGER
     - TINYINT
     - SMALLINT
     - MEDIUMINT
     - BIGINT
     - UNSIGNED BIG INT
     - INT2
     - INT8
  2. TEXT
     - CHARACTER(20)
     - VARCHAR(255)
     - VARYING CHARACTER)(255)
     - NCHAR(55)
     - NATIVE CHARACTER(70)
     - NVARCHAR(100)
     - TEXT
     - CLOB
  3. BLOB
     - no datatype spectified
  4. REAL
     - REAL
     - DOUBLE
     - DOUBLE PRECISION
     - FLOAT
  5. NUMERIC
     - NUMERIC
     - DECIMAL(10, 5)
     - BOOLEAN
     - DATE
     - DATETIME



### SQL

- Structured Query Language
- RDBMS의 데이터 관리를 위해 설계된 특수 목적 프로그래밍 언어
- 스키마 생성 수정
- 자료 검색 관리
- 객체 접근 조정 관리
- DDL - 데이터 정의언어 (Definition)
  - 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어
  - CREATE
  - DROP
  - ALTER
- DML - 데이터 조작 언어 (Manipulation)
  - 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어
  - INSERT
  - SELECT
  - UPDATE
  - DELETE
- DCL - 데이터 제어 언어 (Control)
  - E데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어
  - GRANT
  - REVOKE
  - COMMIT
  - ROLLBACK



### Hello World!

- 데이터베이스 생성하기

```sqlite
$ sqlite3 tutorial.sqlite3
-- sqlite3, tutorial파일좀 sqlite3 형식으로 생성해줘~

sqlite> .database
-- 현재 나의 메인위치는 어디니?
```

- csv 파일을 table로 만들기

```sqlite
sqlite> .mode csv
sqlite> .import hellodb.csv examples
-- csv 모드로한 후, hellodb.csv파일에 있는 것을 examples 파일에 테이블로 만들어줘

sqlite> .tables
-- 테이블의 목록을 좀 보여줘

-- 내 데이터베이스 위치 안에 테이블을 만들게 됨.
-- 데이터베이스 안만들고 테이블 생성하고있어서 엄청 헤맸던 오늘..
```

- 테이블 생성 및 삭제 statument

```sqlite
-- CREATE TABLE, 데이터베이스에서 테이블 생성
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT    
);

-- 스키마 조회
sqlite> .schema classmates

-- 테이블 삭제
DROP TABLE classmates;

```

- 필드 제약 조건
  -  NOT NULL : NULL 값 입력 금지
  - UNIQUE : 중복 값 입력 금지 (NULL 값은 중복 입력 가능)
  - PRIMARY KEY : 테이블에서 반드시 하나 NOT NULL + UNIQUE
  - FOREIGN KEY : 외래키. 다른 테이블의 Key
  - CHECK : 조건으로 설정된 값만 입력 허용
  - DEFAULT : 기본 설정 값
