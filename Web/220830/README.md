## 2022년 8월 30일(화)

> Web! CSS 기본 스타일



**수호아빠의 한줄평 : 처음 강의를 듣고..내가...듣긴 들었는데 뭘 들었는지 몰랐었던..**



### 크기 단위

- PX
  - 모니터 해상도 화소 '픽셀','px' 기준
  - 크기가 변하지 않기 때문에 고정적인 단위
  - 화면 비율이 바뀌어도 고정된다.


- %
  - 백분율 단위 (100%, 50%)
  - 가변적인 레이아웃에서 자주 사용
  - 화면 구성에 따라 크기가 달라짐

- em
  - (바로 위, 부모요소에 대한) 상속에 영향을 받음
  - html의 기본 루트가 16px이라면, em으로 설정 시 32*2의 크기

- rem

  - 상속의 영향을 받지 않음

  - html의 기본 루트가 16px이어도, 32px

  - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐


- vieport

  - 사용자가 바로 보게되는 웹 컨텐츠의 영역 (디바이스 화면)
  - 디바이스에 따라 상대적인 사이즈가 결정됨
  - 예) vw, vh, vmin, vmax

- 색상 단위

  - 색상 키워드 (background-color: red;)
    - red, blue, black 과 같은 특정 색을 직접 글자로 나타낸다.
    - color: red
    - 대소문자 구분 x

  - RGB 색상 (background-color: rgb(0, 255, 0);)
    - color: rgb(0, 255, 0)
    - 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현하는 방식

  - HSL 색상 (background-color: hsl(0, 100%, 50%);)
    - 색상, 채도, 명도로 색상을 표현한다.



### CSS Selectors

- 기본 선택자

  - 요소

  - 클래스

  - id

- 결합자 Combinators

  - 자손 결합자, 자식 결합자

- 의사 클래스/요소 Pseudo Class

  - 링크, 동적 의사 클래스

#### 우선순위

1. !important: 사용시 주의
2. 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
3. css 파일 로딩 순서

#### CSS 상속

- 부모 요소에 상속된다.
  - 모든 폰트를 하나로 통일하고자 할 때 상위 요소만 바꾸면 한 번에 다 바뀌게 되는 편리함이 있다.
- 상속 되는 것
  - (Text: font, color, text-align), opacity, visibility 등
- 상속 되지 않는 것
  - Box model : width, height, margin, padding, border, box-sizing, display
  - position: position, top/right/bottom/left, z-index

### Box model

**모든 요소는 네모네모 박스모델이고, 위에서 아래로, 왼쪽에서 오른쪽으로 쌓인다.**

(좌측 상단으로 모인다고 생각하자)

- 하나의 박스는 네 부분(영역)으로 이루어짐
  1. margin
  2. border
  3. padding
  4. content

- margin
  - 여백
  - 여백 지정 시 margin 상하좌우를 다르게 줄 수 있다.

```
.margin-4 (
    margin: 10px 20px 30px 40px;
)           상    하   좌    우
```

- border
  - 경계선, 테두리
  - border-radius: 원을 만들거나 박스 테두리를 둥글게 깎는다.
- padding
  - 내부 여백
- content
  - 실제 내용이 들어가는 곳
  - 내용이 없으면 상단요소들이 생성되지 않는다.

### CSS Display

display 크기에 따라 **배치**가 달라진다.

#### display: block

- 줄 바꿈이 일어나는 요소
- 가로폭을 차지한다.
- div는 block에 상응하고, 줄바꿈을 이룬다.
  - 오른쪽을 모두 마진으로 채워서 줄바꿈을 하도록 한다.
  - 줄바꿈을 없애고자 margin-right: 0 ;으로 해도 변경되지 않는다.
  - 줄바꿈을 없애고자 할 때는 **display: inline-bock으로 설정해야 한다.**
- 가운데 정렬: margin: 0 auto;
- 오른쪽 정렬: margin-left: auto;
- 블록 레벨 요소
  - div / ul, ol, li / p / hr / form

#### display: inline

- 줄 바꿈이 일어나지 않는다.
- 컨텐츠 너비만큼 가로 폭을 차지한다.
- width, height, margin-top, margin-bottom 기능들을 사용할 수 없다.
- span은 inline에 상응한다.
  - span / a / img / input, label / b, em, i, strong

#### display: none

- 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않는다.
- 구글에 로그인할 때 차례대로 아이디와 비번을 치게 된다.
  - 아이디와 비번을 치는 그 공간이 display: none으로 이루어져있다.
  - 아이디를 치는 공간에서 비번을 치는 공간으로 넘겨주기 위해 존재한다.
- 이외 다양한 display 속성은 https://developer.mozilla.org/ko/docs/Web/CSS/display



## 오후 실습

[오후실습! 주어진 이미지와 비슷하게 만들어보기](./practice.md)

