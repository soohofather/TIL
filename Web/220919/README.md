## 2022년 9월 19일(월)

> Web-JavaScript03! 



**수호아빠의 한줄평: 음...콜록콜록....파이썬이랑 비슷한거 같긴한데.. 왜이렇게 이질감 느껴지고 어렵지..**



`오늘의 코드 01`

```html
<body>

  <input type="text" id="text-input">

  <script>
    const textInput = document.querySelector('#text-input')
    textInput.addEventListener('input', function(event){
      console.log(event.target.value)

    })
  </script>
</body>
```

### 인풋 박스에 입력한 데이터 정보를 받기

- function함수를 사용해서 event 라고 지정한 함수값의 target.value 값을 받기
- 딱 입력된 값의 정보를 받을수 있음. 지우면 지운 상태의 값



`오늘의 코드 02`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .modal-overlay {
      background-color: rgba(0, 0, 0, 0.8);
      width: 100%;
      height: 100vh;

      position: fixed;
      top: 0;
      left: 0;

      color: white;
      display: flex;
      justify-content: center;
      align-items: center;
      display: none;
    }
    .active{
      display: flex;

    }
  </style>
</head>
<body>
  <button id="modal-btn">모달 버튼</button>
  <div id="modal-content" class="modal-overlay">모달달 <button id="modal-cancel">닫기</button></div>

  <script>
    const modalBtn = document.querySelector('#modal-btn')
    modalBtn.addEventListener('click', function(){
      document.querySelector('#modal-content').classList.toggle('active')
    })
    const modalCancel = document.querySelector('#modal-cancel')
    modalCancel.addEventListener('click', function(){
      document.querySelector('#modal-content').classList.toggle('active')
    })

  </script>
  
</body>
</html>
```

###  motal 만들기

1. 처음 버튼을 먼저 만들었고,
2. 그 후 까만색 꽉차는 것을 만들었는데 버튼 아래에 생성되었다.
3. 그래서 포지션을 픽스드하여 탑, 레프트 0으로 설정하였다.
4. 그러니 1번에서 만들었떤 버튼위로 설정되어 버튼이 눌려지지 않았고,
5. 디스플레이 none으로 설정하였다. 이후 버튼을 누르면 다시 화면에 나타나게 할 것이다.
6. 그것을 자바스크립트로 설정하였고,
7. 처음 쿼리 셀렉터로 원하는 아이디를 가져와서
8. addEventListener를 사용하여 7번에서 가져온것이 실행이 되면 어떻게 할것이냐를 설정하였다.
9. toggle이란 것으로 active를 한다 끈다 한다 끈다를 설정하였다.
10. active는 디스플레이 flex 설정으로 기존에 none인게 키면 flex가 되어 화면에 나타난다.
11. 여기서 문제는 나타났을떄 다시 끄는것이 없었다.
12. 그래서 다시 나타난 화면에서 버튼을 만들어서 그 버튼을 누르면 디스플레이가 다시 none 되도록 toggle을 사용하여 만들었다.

`오늘의 코드 03`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .carousel-items{
      position: relative;
      display: flex;
      width: 10rem;
      height: 10rem;
      overflow: hidden;
    
    }
    .carousel-item{
      position: absolute;
      top: 0;
      width: 10rem;
      height: 10rem;
      background-color: bisque;
      display: none;

    }
    .active{
      display: block;
      animation: active 2s;
    }
    @keyframes active {
      0% {
        transform: translatex(100%);
       }
      100% {
        transform: translatex(0);
        }
      }

  </style>
</head>
<body>
  <div class="container">
    <div class="carousel-items">
      <div class="carousel-item active">1</div>
      <div class="carousel-item">2</div>
      <div class="carousel-item">3</div>
      <div class="carousel-item">4</div>
    </div>
  </div>

  <button id="next-btn">NEXT</button>

  <script>
    const nextBtn = document.querySelector('#next-btn')
    nextBtn.addEventListener('click', function(){
      
      const currentElement = document.querySelector('.active ')

      const items = document.querySelectorAll('.carousel-item')

      const idx = [...items].indexOf(currentElement)

      console.log(currentElement, items, idx)

      currentElement.classList.toggle('active')
      items[(idx+1)%items.length].classList.toggle('active')
      
    })


  </script>
  
</body>
</html>
```

### 자바스크립트로 화면 넘기기 구현하기!

1. 일단 가로세로 10rem사이즈 네모를 4개를 먼저 만들었고

2. 그 네개를 묶어서 디스플레이 flex를 주었다.

3. 그리고 그 네모들 아래에 next라는 버튼을 만들었다.

4. 현재는 네개의 네모중 가장 첫번째만 display를  block(나타나게)하였고, 나머지는 none으로 설정하였다.

5. 이제 자바스크립트를 사용하여 3번에서 만든 버튼을누르면 지금 현재의 네모의 디스플레이는  none으로 이 다음 번호의 네모의 디스플레이는 block로 상태를 변경하게 할것이다.

6. 여기서 가장 중요한건 인덱스다. 현재의 위치.

7. querySelectorAll를 사용하여 변수에다가 집어 넣는다.

8. const idx = [...items].indexOf(currentElement)는 현재의 값의 인덱스가 몇인가를 7번에서 찾는 것이다.

9. 그 찾는 것을 사용하여 지금의 위치는 none으로 toggle하고, 현재의 위치 + 1에는 active로 toggle 한다.

10. 마지막에서 다시 처음으로 가는것을 정하기 위한 공식이 필요하다

    지금 인덱스의 나누기 전체길이를 하고 나머지로 하는것이다. 1을 원하면 1 나누기 5하면 나머지가 1... 

    이렇게 가다가 5 나누기 5하면 다시 1이 되어 1부터 시작할 수 있게한다.

​	
