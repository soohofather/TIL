## 2022년 9월 1일(목)

> 오후실습! 주어진 사진과 같이 만들기



**수호아빠의 한줄평 : 아..힘들다.. 뭔가 약간 간질간질 짜증나는 느낌... 지치네 휴.. 2번은 정렬 실패**



### 실습 1

![image-20220901174740470](assets/image-20220901174740470.png)

**HTML**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="css/_reset.css">
  <link rel="stylesheet" href="css/style.css">
  <title>HPHK APPAREL</title>
</head>
<body>
  <nav class="nav">
    <h1 class="nav-a" href="">APPAREL SHOP</h1>
    <ul class="nav-list">
      <li class="nav-item">
        <a class="nav-a" href="">HOME</a>
      </li>
      <li class="nav-item">
        <a class="nav-a" href="">PRODUCTS</a>
      </li>
    </ul>
  </nav>
  <div class="top-btn">
    <img src="../assets/up-arrow.png">
  </div> 
  <section class="section">
    <div class="banner"></div>
    <div class="div-1">
      <img class="about-img" src="../assets/apparel2.jpeg">
      <div class="div-2">
        <h2 class="about_more_font">About Our Company</h2>
        <p class="content_font">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias delectus sunt hic, veniam consequuntur repellat dolor sapiente? Veritatis laboriosam iste quisquam assumenda ex quo ad neque recusandae voluptatibus, veniam autem obcaecati officiis ratione iure esse labore pariatur error voluptatum numquam culpa cupiditate magnam? Quas minima maiores tempora optio maxime obcaecati, ipsum quae pariatur sed officia. Error perferendis dolorum labore ea!
        </p>
      </div>
    </div>
    <div>
      <h2 class="about_more_font">more</h2>
      <div class="div-3">
        <div class="div_4">
          <img class="about-img2" src="../assets/email.png">
          <p>Email Address<br>hphker@hphk.kr</p>
        </div>
        <div class="div_4">
          <img class="about-img2" src="../assets/telephone.png">
          <p>Phone Number<br>010-1234-5678</p>
        </div>
        <div class="div_4">
          <img class="about-img2" src="../assets/location.png">
          <p>Location<br>서울특별시</p>
        </div>
        <div class="div_4">
          <img class="about-img2" src="../assets/clock.png">
          <p>Working Hours<br>9am~6pm</p>
        </div>
      </div>
    </div>
  </section>
</body>
</html>
```

```css
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="css/_reset.css">
  <link rel="stylesheet" href="css/style.css">
  <title>HPHK APPAREL</title>
</head>
<body>
  <nav class="nav">
    <h1 class="nav-a" href="">APPAREL SHOP</h1>
    <ul class="nav-list">
      <li class="nav-item">
        <a class="nav-a" href="">HOME</a>
      </li>
      <li class="nav-item">
        <a class="nav-a" href="">PRODUCTS</a>
      </li>
    </ul>
  </nav>
  <div class="top-btn">
    <img src="../assets/up-arrow.png">
  </div> 
  <section class="section">
    <div class="banner"></div>
    <div class="div-1">
      <img class="about-img" src="../assets/apparel2.jpeg">
      <div class="div-2">
        <h2 class="about_more_font">About Our Company</h2>
        <p class="content_font">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias delectus sunt hic, veniam consequuntur repellat dolor sapiente? Veritatis laboriosam iste quisquam assumenda ex quo ad neque recusandae voluptatibus, veniam autem obcaecati officiis ratione iure esse labore pariatur error voluptatum numquam culpa cupiditate magnam? Quas minima maiores tempora optio maxime obcaecati, ipsum quae pariatur sed officia. Error perferendis dolorum labore ea!
        </p>
      </div>
    </div>
    <div>
      <h2 class="about_more_font">more</h2>
      <div class="div-3">
        <div class="div_4">
          <img class="about-img2" src="../assets/email.png">
          <p>Email Address<br>hphker@hphk.kr</p>
        </div>
        <div class="div_4">
          <img class="about-img2" src="../assets/telephone.png">
          <p>Phone Number<br>010-1234-5678</p>
        </div>
        <div class="div_4">
          <img class="about-img2" src="../assets/location.png">
          <p>Location<br>서울특별시</p>
        </div>
        <div class="div_4">
          <img class="about-img2" src="../assets/clock.png">
          <p>Working Hours<br>9am~6pm</p>
        </div>
      </div>
    </div>
  </section>
</body>
</html>
```



**수호아빠 결과물**

![image-20220901174918413](assets/image-20220901174918413.png)



### 실습 2

![image-20220901175034045](assets/image-20220901175034045.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="css/_reset.css">
  <link rel="stylesheet" href="css/style.css">
  <title>Shop Example</title>
</head>
<body>
  <nav class="nav">
    <h1 class="nav-a" href="">APPAREL SHOP</h1>
    <ul class="nav-list">
      <li class="nav-item">
        <a class="nav-a" href="">HOME</a>
      </li>
      <li class="nav-item">
        <a class="nav-a" href="">PRODUCTS</a>
      </li>
    </ul>
  </nav>
  <div class="products">
    <div class="div_5">
      <img src="../assets/temp.jpg" class="card-img">
      <h2 class="category_name">T-shirts</h2>
      <p class="content_font_2">
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Magni excepturi nihil architecto deleniti impedit nam, possimus blanditiis omnis rerum earum provident perspiciatis quam incidunt at amet beatae velit quod dolorum?
      </p>
    </div>
    <div class="div_5">
      <img src="../assets/temp.jpg" class="card-img">
      <h2 class="category_name">Slacks</h2>
      <p class="content_font_2">
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Magni excepturi nihil architecto deleniti impedit nam, possimus blanditiis omnis rerum earum provident perspiciatis quam incidunt at amet beatae velit quod dolorum?
      </p>
    </div>
    <div class="div_5">
      <img src="../assets/temp.jpg" class="card-img">
      <h2 class="category_name">Jeans</h2>
      <p class="content_font_2">
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Magni excepturi nihil architecto deleniti impedit nam, possimus blanditiis omnis rerum earum provident perspiciatis quam incidunt at amet beatae velit quod dolorum?
      </p>
    </div>
    <div class="div_5">
      <img src="../assets/temp.jpg" class="card-img">
      <h2 class="category_name">Shoes</h2>
      <p class="content_font_2">
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Magni excepturi nihil architecto deleniti impedit nam, possimus blanditiis omnis rerum earum provident perspiciatis quam incidunt at amet beatae velit quod dolorum?
      </p>
    </div>
    <div class="div_5">
      <img src="../assets/temp.jpg" class="card-img">
      <h2 class="category_name">Suits</h2>
      <p class="content_font_2">
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Magni excepturi nihil architecto deleniti impedit nam, possimus blanditiis omnis rerum earum provident perspiciatis quam incidunt at amet beatae velit quod dolorum?
      </p>
    </div>
    <div class="div_5">
      <img src="../assets/temp.jpg" class="card-img">
      <h2 class="category_name">Accessories</h2>
      <p class="content_font_2">
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Magni excepturi nihil architecto deleniti impedit nam, possimus blanditiis omnis rerum earum provident perspiciatis quam incidunt at amet beatae velit quod dolorum?
      </p>
    </div>
  </div>
 
</body>
</html>
```

```css
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="css/_reset.css">
  <link rel="stylesheet" href="css/style.css">
  <title>HPHK APPAREL</title>
</head>
<body>
  <nav class="nav">
    <h1 class="nav-a" href="">APPAREL SHOP</h1>
    <ul class="nav-list">
      <li class="nav-item">
        <a class="nav-a" href="">HOME</a>
      </li>
      <li class="nav-item">
        <a class="nav-a" href="">PRODUCTS</a>
      </li>
    </ul>
  </nav>
  <div class="top-btn">
    <img src="../assets/up-arrow.png">
  </div> 
  <section class="section">
    <div class="banner"></div>
    <div class="div-1">
      <img class="about-img" src="../assets/apparel2.jpeg">
      <div class="div-2">
        <h2 class="about_more_font">About Our Company</h2>
        <p class="content_font">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias delectus sunt hic, veniam consequuntur repellat dolor sapiente? Veritatis laboriosam iste quisquam assumenda ex quo ad neque recusandae voluptatibus, veniam autem obcaecati officiis ratione iure esse labore pariatur error voluptatum numquam culpa cupiditate magnam? Quas minima maiores tempora optio maxime obcaecati, ipsum quae pariatur sed officia. Error perferendis dolorum labore ea!
        </p>
      </div>
    </div>
    <div>
      <h2 class="about_more_font">more</h2>
      <div class="div-3">
        <div class="div_4">
          <img class="about-img2" src="../assets/email.png">
          <p>Email Address<br>hphker@hphk.kr</p>
        </div>
        <div class="div_4">
          <img class="about-img2" src="../assets/telephone.png">
          <p>Phone Number<br>010-1234-5678</p>
        </div>
        <div class="div_4">
          <img class="about-img2" src="../assets/location.png">
          <p>Location<br>서울특별시</p>
        </div>
        <div class="div_4">
          <img class="about-img2" src="../assets/clock.png">
          <p>Working Hours<br>9am~6pm</p>
        </div>
      </div>
    </div>
  </section>
</body>
</html>
```

**수호아빠의 결과물**

![image-20220901175125692](assets/image-20220901175125692.png)
