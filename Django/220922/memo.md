## 2022년 9월 22일(목)

> Django02! 



- 장고야 프로젝트를 시작해줘.
  - django-admin startproject firstpjt. 

- 애플리케이션(앱) 생성

  - python manage.py startapp articles

  - config = 설정하다

  - 가장중요한 파일을 꼽으라면 views 파일 ★

  - 생성 후에 등록을 해줘야함.

  - firstpjt에 setting에 INSTALLED_APPS에 장고가 설치된 것을 알아서 넣어줌

  - 장고에게 툭툭 던지는 느낌. 장고가 해줌

  - 일꾼형식 IMPERATIVE 명령 (스프넣어, 물빼, 등등.. 단계적으로) 알고리즘

  - declaretive 선언(묘사) (어..짜장면을 먹고 싶네~ -> 장고가 만들어줌(로직을 가지고있음))

    유지보수가 좋다고 함

  - firstpjt에 setting에 INSTALLED_APPS에 위에서 생성한 `'articles',`를 추가해줌 (맨위에)

  -  하나의 기능은 하나의 앱에서(장고에서는)

  - 웹서비스는 서비스인데, 웹이라는 매개를 사용하는 서비스

  - 이것은 요청과 응답 요청없이 응답이 오지 않음.

  - url로 요청하고 html을 받는것

  - url로 요청받고 html을 보내는 것

  - client(나, 크롬) -> 시세가 담긴 html을 내놔 request -> 네이버 (server)

  - 서버로서 할 일

    1. 주문서 정의 -> URL
    2. 로직 구현 -> VIEW
    3. html 페이지 구성 -> TEMPLATE

  - firstpjt -> urls.py -> path('index/',  어떤 view 파일에서)

    - from articles import views
    - path('index/', views.index),

  - articles -> views.py

    - def index(request):

      return render(request, 'index.html')

    - 3번째에는 딕셔너리 가능 (이름은 아무거나 상관없지만, context로 보통 지음)

      return render(request, 'index.html', context)

    -   context = {

      ​    'name': '이동현',

      ​    'img' : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDiIpYwOZlJKPYs-mzipYDPiqeCldvAHyYaQ&usqp=CAU'

        }

    - def index(request):

      

        names = ['1', '2', '3', '4', '5']

        name = random.choice(names)

      

        context = {

      ​    'name': name,

      ​    'img' : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTd4NhIl-ezEPr20Dwvx9kHUo3d3aiKug-nZg&usqp=CAU'

        }

      

    
        return render(request, 'index.html', context)
    
    - \<img src="{{ img }}">
    
    - path('welcome/\<name>', views.welcome),
    
      welcome은 함수이름

​	
