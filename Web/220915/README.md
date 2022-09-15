## 2022년 9월 15일(목)

> Web-JavaScript01! 자바스크립트 맛보기!



**수호아빠의 한줄평: 복습을 했는데도 뭔말인지 어떻게 써야하는건지 모르겠네....**



## JavaScript

### JavaCript란?

- [HTML](https://developer.mozilla.org/ko/docs/Glossary/HTML)은 웹 콘텐츠의 구조를 짜고 의미를 부여하는 마크업 언어입니다. 예를 들어 페이지의 어디가 문단이고, 헤딩이고, 데이터 표와 외부 이미지/비디오인지 정의합니다.
- [CSS](https://developer.mozilla.org/ko/docs/Glossary/CSS)는 HTML 콘텐츠에 스타일을 적용할 수 있는 스타일 규칙 언어입니다. 배경색을 추가하고, 글꼴을 바꾸고, 콘텐츠를 신문처럼 다열 레이아웃으로 배치할 수 있습니다.
- [JavaScript](https://developer.mozilla.org/ko/docs/Glossary/JavaScript)는 동적으로 콘텐츠를 바꾸고, 멀티미디어를 제어하고, 애니메이션을 추가하는 등 거의 모든 것을 만들 수 있는 스크립팅 언어입니다. (정말 모든게 가능하지는 않겠지만, JavaScript 코드 몇 줄만으로도 놀라운 결과를 이룰 수 있습니다)

### 웹 페이지에 JavaScript를 넣는 방법

- CSS와 비슷한 방법으로 JavaScript를 HTML 코드에 적용할 수 있습니다. CSS가 \<link> 요소로 외부 스타일 시트를 적용하고, \<style>요소로 내부 스타일 시트를 적용했다면, JavaScript는 한 종류의 HTML 친구만 요구합니다. 바로 \<script> 요소입니다.

```html
<script>

  // JavaScript goes here

</script>
```

### 브라우저에서 할 수 있는 일

- DOM 조작
- BOM 조작
- JavaScript Core (ECMA Script)

### DOM 조작

- DOM이란?

  - HTML, XML과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스
  - 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델
  - 문서가 구조화되어 있으며 각 요소는 객체(object)로 취급
  - 단순한 속성 접근, 메서드 활용뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
  - window : DOM을 표현하는 창. 가장 최상위 객체 (작성 시 생략 가능)
  - 파싱(Parsing) : 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정

  

- DOM 조작 순서 (선택하고, 변경한다)

  1. 선택 (Select)
     - querySelector()
     - querySelectorAll()
     - 기타 등등
  2. 변경 (Manipulation)
     - innerText
     - innerHTML
     - element.style.color
     - setAttribute()
     - getAttribute()
     - createElement()
     - appendChild()
     - 기타 등등

  

- DOM 객체의 상속 구조

  - EventTarget
  - Node
  - Element
  - Document
  - HTML Element



#### DOM 선택

- DOM 선택 관련 메서드 1
  - document.querySelector(selector)
  - document.querySelectorAll(selector
  - querySelector(), querySelectorAll()을 사용하는 이유
    - id, class 그리고 tag 선택자 등을 모두 사용 가능하므로, 더 구체적이고 유연하게 선택 가능 
    - ex) document.querySelector('#id’), document.querySelectAll(‘.class')

```html
<script>
  // 선택자를 활용해 선택할 때 
  // 하나를 선택한다. => querySelector
  // 모든 결과를 선택한다. => querySelectorAll

  console.log(document.querySelector('#title'))
  // <h1 id="title">JS 기초</h1>
  console.log(document.querySelectorAll('.text'))
  // NodeList(2) [p.text, p.text]
  console.log(document.querySelector('.text'))
  // <p class="text">querySelector</p>
</script>
```

- DOM 선택 관련 메서드 2

  - getElementById(id)
  - getElementsByTagName(name)
  -  getElementsByClassName(names)

  

- 선택 메서드별 반환 타입

  - 단일 element
    - getElementById()
    - **querySelector()**
  - HTML Collection
    - getElementsByTagName()
    - getElementsByClassName()
  - NodeList
    - **querySelectorAll()**



- HTML Collection & NodeList

  - 둘 다 배열과 같이 각 항목에 접근하기 위한 index를 제공 (유사 배열)

  - HTML Collection

    - name, id, index 속성으로 각 항목에 접근 가능

  - NodeList

    - index로만 각 항목에 접근 가능
    - 단, HTMLCollection과 달리 배열에서 사용하는 forEach 메서드 및 다양한 메서드 사용 가능

  - 둘 다 Live Collection으로 DOM의 변경사항을 실시간으로 반영하지만, 

    **querySelectorAll()에 의해 반환되는 NodeList는 Static Collection으로 실시간으로 반영되지 않음**



- Collection
  - Live Collection
    - 문서가 바뀔 때 실시간으로 업데이트 됨
    - DOM의 변경사항을 실시간으로 collection에 반영
    - ex) HTMLCollection, NodeList
  - Static Collection (non-live)
    - DOM이 변경되어도 collection 내용에는 영향을 주지 않음
    - querySelectorAll()의 반환 NodeList만 static collection



#### DOM 변경

- 변경 관련 메서드 (Creation DOM)
  - document.createElement()
    - 작성한 태그 명의 HTML 요소를 생성하여 반환



- 변경 관련 메서드 (append DOM)

  - Element.append()
    - 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 Node 객체나 DOMString을 삽입
    - 여러 개의 Node 객체, DOMString을 추가 할 수 있음
    - 반환 값이 없음

  - Node.appendChild()
    - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입 (Node만 추가 가능)
    - 한번에 오직 하나의 Node만 추가할 수 있음
    - 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 새로운 위치로 이동



- ParentNode.append() vs Node.appendChild()
  - append()를 사용하면 DOMString 객체를 추가할 수도 있지만, .appendChild()는 Node 객체만 허용
  - append()는 반환 값이 없지만, appendChild()는 추가된 Node 객체를 반환
  - append()는 여러 Node 객체와 문자열을 추가할 수 있지만, .appendChild()는 하나의 Node 객체만 추가할 수 있음



- 변경 관련 속성(property)
  -  Node.innerText
    - Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현 (해당 요소 내부의 raw text) (사람이 읽을 수 있는 요소만 남김)
    -  즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현
  - Element.innerHTML
    - 요소(element) 내에 포함된 HTML 마크업을 반환
    -  [참고] XSS 공격에 취약하므로 사용 시 주의

​	

- XSS (Cross-site Scripting)
  - 공격자가 입력요소를 사용하여 웹 사이트 클라이언트 측 코드에 악성 스크립트를 삽입 해 공격하는 방법
  - 피해자(사용자)의 브라우저가 악성 스크립트를 실행하며 공격자가 엑세스 제어를 우회하고 사용자를 가장 할 수 있도록 함



#### DOM 삭제

- 삭제 관련 메서드
  -  ChildNode.remove()
    - Node가 속한 트리에서 해당 Node를 제거
  - Node.removeChild()
    - DOM에서 자식 Node를 제거하고 제거된 Node를 반환
    - Node는 인자로 들어가는 자식 Node의 부모 Node



- 속성 관련 메서드
  - Element.setAttribute(name, value)
    - 지정된 요소의 값을 설정
    - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가
  - Element.getAttribute(attributeName)
    - 해당 요소의 지정된 값(문자열)을 반환
    - 인자(attributeName)는 값을 얻고자 하는 속성의 이름
