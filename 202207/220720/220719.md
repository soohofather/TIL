## 2022년 7월 20일(수)

> 파이썬! 클래스(class)에 대한 심화 내용!!



**수호아빠의 한줄평 : **

​	**클래스를 알아보도록 하자... 다음에 알아보도록 하자..**



### 1. 클래스 (class)



- 클래스 속성 <classname>.<name>으로 접근 및 할당
- namespace : 인스턴스와 클래스간의 이름 공간
- @classmethod(클래스메소드) : 데코레이터를 사용하여 정의, (호출시, 첫번째 인자로 cls가 전달됨)
  - 데코레이터 : 함수를 어떤 함수로 꾸며서 새로운 기능 부여
- @staticmethod(스태틱메소드) : 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메소드
  - 속성을 다루지 않고 단지 기능(행동)만을 하는 메소드 정의할 때 사용

```python
class Myclass:
    
    def method(self):
        return 'instance method', self
    
    @classmethod
    def classmethod(cls):
        return 'class method', cls
    
    @staticmethod
    def staticmethod():
        return 'static method'
```



### 2. 객체 지향의 핵심개념



- 객체지향의 핵심 4가지

  - 추상화
    - 어떤 기능을 만들어 놓고, 그 기능을 사용하기 위한 메서드를 만드는 것
  - 상속
    - 두 클래스 사이 부모 - 자식 관계를 정립
    - 클래스는 상속이 가능하여 object를 상속 받음
    - 부모클래스의 속성, 메소드가 자식 클래스에 상속되므로, 코드 재사용성이 높아짐
    - issubclass(class, classinfo) : class가 classinfor의  subclass면 true
    - super() : 자식클래스에서 부모클래스를 사용하고 싶은 경우
    - 상속 관계에서의 이름 공간은 인스턴스, 자식 클래스, 부모 클래스 순으로 탐색
    - 두개 이상의 클래스를 상속 받는 경우 상속 받은 모든 클래스의 요소를 활용 가능함
  - 다형성 (Polymorphism)
    - 동일한 메소드가 클래스에 따라 다르게 행동할 수 있음
    - 서로 다른 클래스에 있는 객체들이 동일한 메시지에 대해 다른 방식으로 응답 가능
    - 메소드 오버라이딩 : 상속 받은 메소드를 재정의, 상속 받은 기능에서 특정 기능만 바꾸고 싶을때 사용

  - 캡슐화

    - 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 엑세스 차단

    - 파이썬의 기능으로는 존재하지 않지만, 관용적으로 사용되는 표현이 존재

    - 접근 제어자

      - Public Access Modifier

        - 언더바 없이 시작하는 메소드나 속성
        - 어디서나 호출이 가능, 하위 클래스 override 허용

      - Protected Access Modifier

        - 언더바 1개로 시작하는 메소드나 속성
        - 암묵적 규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능

      - Private Access Modifier

        - 언더바 2개로 시작하는 메소드나 속성
        - 본 클래스 내부에서만 사용이 가능

        
