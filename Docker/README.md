### 도커 이미지 설치

- docker run --name python-01 python:3.10-alpine3.15

---

### 도커 생성 후 실행

- docker run --name python-02 python:3.10-alpine3.15 ash

---

### 목록 보기

- docker ps -a : 도커 목록 보여줌
- docker images : 도커 이미지들을 보여줌

---

### 종료

- exit

---

### 컨테이너에 들어가기 (실행중이어야함)

- docker exec -it python-03 ash
  - python-03 대신 ID값도 가능

---

### 만든 이미지로 컨테이너 실행

- docker run -it --name python-04 python:test ash
  - python-04 : 생성 이름
  - python:test : 이미지 이름
  - ash : 쉘 이름

