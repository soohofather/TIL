# 마크다운

> 마크다운은 plain text 기반의 마크업 언어의 일종이다. 

## 제목/소제목 (Heading)

`#`의 개수에 따라 `h1` ~ `h6`까지 표현 가능하다.

### h3

#### h4

##### h5

###### h6

## 목록 (list)

### 순서가 없는 리스트 : `-`(hypen), `*`(asterisk) 

목록 활용시 단계를 `tab`과 `shift + tab`으로 조절한다.

- 사과 
- 바나나
  - 미니 바나나
  - Dole 바나나 
- 딸기
  - 산딸기
- 복숭아
  - 백도 복숭아
  - 천도 복숭아

### 순서가 있는 리스트 : 1. 

아침에 일어나서 KDT 교육 듣기

1. 세수하고 양치
2. 산책
3. Syllaverse 홈페이지 접속한다.
   1. 로그인
   2. 대시보드 확인
4. 유튜브 라이브에 접속한다.
   1. 인사를 남긴다.

## 코드 블록

### Fenced Code Block

* `(backtick) 기호 3개를 활용하여 작성한다. 
* 특정 언어를 명시하면 Syntax highlighting 기능이 적용된다.

```python
print('hello')

if True:
    print('t')
else:
    print('f')
# 주석

print('happy hacking!')

if True:
    print('참')
else:
    print('거짓')
```

```html
print('hello')
# 주석?
<h1>
    제목
</h1>
<!-- 주석 -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>마크다운</h1>
    <ul>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
    </ul>
</body>
</html>
```

### Inline Code block

`print` 는 파이썬에서 출력하는 함수이다.

## 링크

[실라버스 링크](https://syllaverse.com)



## 이미지

![](C:\Users\hphk\Desktop\hphk.png)

* 아래의 이미지는 나오지 않음. 
  * 절대경로 (C드라이브 ~)

![bonobono](C:\Users\hphk\Desktop\bonobono.png)

* 아래의 이미지는 나옴
  * 상대경로
  * 마크다운.assets 폴더를 같이 공유하면!

![bonobono](마크다운.assets/bonobono.png)

## 인용문

> Life is short, you need python. 



## 표

타이포라 기능을 적극 활용하자. 

본문 > 표 > 표 삽입 (ctrl + t)

| 이름  | 댓글                               |
| ----- | ---------------------------------- |
| 류진X | 노션이랑 비슷하네요                |
| 이성X | 빨간색 노란색 프로그램 무엇인가요? |
|       |                                    |

## 텍스트 

**굵게(볼드체)** : `**`

*기울림(이탤릭체)* : `*`

~~취소선~~ : `~~`



## 수평선

`---`

---



## ✔ 기타 정리

띄어 쓰기 있는 것

* 제목 (`#`)
* 목록 (`-`, `1.`)

띄어 쓰기 없는 것

`inline code block` *기울임* **굵게**

***기울임굵게***

이모지 : window + .













