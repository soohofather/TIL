## 2022년 9월 16일(금)

> Web-JavaScript02! 수업을 못따라가서..독학시간..



**수호아빠의 한줄평: 오늘은 수업내용을 전체적으로 못따라감. 다른곳에서 기초검색해서 기초공부중..출처 유투버 드림코딩**



## 데이터타입

### 1. Variable - 변수

`let`, `var`

#### let (added in ES6)

- 아래와 같이 name = elite로 선언했다가, 다시 hello로 재선언 가능

```html
<script>
    let name = 'elite'; 
    console.log(name); // elite 출력
    name = 'hello';
    console.log(name); // hello 출력
</script>
```

- {} 블록 스코프 - 블록안에 있는 것들은 밖에서 출력할 수 없음

```html
<script>
    {    
        let name = 'elite'; 
        console.log(name);
        name = 'hello';
        console.log(name);
    }
    console.log(name;) // 아무값도 나오지 않음
</script>
```

- 글로벌한 변수(let globalName)는 어디서든 출력할 수 있음

```html
<script>
    let globalName = 'global name';
    {    
        let name = 'elite'; 
        console.log(name);
        name = 'hello';
        console.log(name);
        console.log(globalName); // global name 출력
    }
	console.log(globalName);	// global name 출력
</script>

```

- 최근에는 변수에 모두 let을 씀
- ES6이전에는 var를 썻었음

### var

- 변수를 지정하지 않은 상태에서 먼저 값을 넣고 변수를 지정해도 진행 가능.

```html
<script>
    
    console.log(age); // 변수가 정해지지 않았는데도 undefined 출력
	age = 4;          
    console.log(age); // 값을 넣자 변수가 정해지지 않았는데도 4 출력
	var age;

</script>
```

```html
<script>
    
    name = 4;
	let age; // 에러 뜸. 변수 name이 선언되지 않은 상태에서 4를 넣음

</script>
```

- var hoisting (move declaration from bottom to top)
  - var는 has no block scope \
  - {} 있고 없고 차이 없음.

- 이러한 이유들로 인해 이전에는 불안해도 var를 썼으나, 현재 let이 생기고 let을 쓰기 시작

### 2. Constants 

`const`

- 한번 값을 할당하면 절대 값이 변하지 않는 것
- 장점
  - 보안성 security
  - 스레드 안정성 thread safety
  - 사람 실수 줄여줌 reduce human mistakes

```html
<script>
    
    const daysInweek = 7;
    const maxNumber = 5;

</script>
```

- 정리
  - Mutable (변경 가능한) : let
  - Immutable (변경 불가능한) : const

### 3. Variable types

`number` `string` `boolean` `null` `undefined` `symbol` `object`

 `function` `first-class funtion`

#### number

- 자바스트립트에서는 숫자는 number 1개로 끝 (다른 언어는 float,int 블라 블라)

```html
<script>
    
    const count = 17; // type: number
	const size = 17.1; // type:number
	console.log(`value: ${count}, type: ${typeof count}`)
	console.log(`value: ${size}, type: ${typeof size}`)

</script>
```

- 기타 number

```html
<script>
    const infinity = 1 / 0;				// type: infinity
    const negativeInfinity = -1 / 0;	// type: negativeInfinity
    const nAn = 'not a number' / 2;		// type: nAn
    console.log(infinity);
    console.log(negativeInfinity);
    console.log(nAn);
</script>
```

- 자바스크립트에서는 -2의 53승부터 2의 53승까지 (-2**53) ~ (2**53)
  - 최근에 bigInt가 추가됨, 아직 크롬이랑 파이어폭스만 됨

```html
<script>
    const bigInt = 78903450893450892348092349082345234n // 끝에 n
    console.log(`value: ${bigInt}, type: ${typeof bigInt}`)
</script>
```

#### string

- 자바스크립트에서는 한개나, 여러개의 글자든 모두 string

```html
<script>
    const char = 'c'
    const brendan = 'brendan';
    const greeting = 'hello ' + brendan;
    console.log(`value: ${greeting}!`);
    const helloBob = `hi ${brendan}!`;
    console.log(`value: ${helloBob} type: ${typeof helloBob}`) // type : string
    console.log('value: ' + helloBob + ' type: ' + typeof helloBob) 
    // type : string
</script>
```

#### boolean

- False
  - 0, null, undefined, NaN, ''
- True
  - 그 외

```html
<script>
    const canRead = true;
    const test = 3 < 1;
    console.log(`value: ${canRead} type: ${typeof canRead}`) // true
    console.log(`value: ${test} type: ${typeof test}`)		 // true
</script>
```

#### null과 undefined

- null은 ''내가 너는 null이야''라며 지정한것

```html
<script>
    let nothing = null;
	console.log(`value: ${nothing}, type: ${typeof nothing}`)
</script>
```

- undefined은 값을 출력을 하려는데 아무것도 없어서 나오는 것

```html
<script>
    let x;
    console.log(`value: ${x}, type: ${typeof x}`);
</script>
```

#### symbol

- 고유한 식별자가 필요할때 씀

```html
<script>
    const symbol1 = Symbol('id');
    const symbol2 = Symbol('id');
    console.log(symbol1 === symbol2); // 위의 두개가 같은걸 넣어도 false 나옴
    const gSymbol1 = Symbol.for('id');
    const gSymbol2 = Symbol.for('id');
    console.log(gSymbol1 === gSymbol2); // true
</script>
```

- symbol은 타입을 조회할때 .description을 사용하여 string으로 만들어줘야함

```html
<script>
    console.log(`value: ${symbol1.description}, type: ${typeof symbol1}`)
</script>
```

#### object

- real-life object, date structure
- number, string, boolean, null, undefined, symbol것들을 하나로 묶어서 한 박스나 컨테이너로 관리

```html
<script>
	const ellie = { name: 'ellie', age: 20 };
    // ellie는 const로 선언되어 변경 불가능하지만
	// name과 age는 변경가능
    ellie.age = 21; // age: 21

</script>
```

### 4. Dynamic typing: dynamically typed language

- 런타임, 즉 위에서부터 내려가면서 타입이 막 스트링이었다가, 넘버였다가로 변경이 됨

```html
<script>
    let text = 'hello';
    console.log(`value: ${text}, type: ${typeof text}`)
    // 출력 값 hello, 타입 string
    
    text = 1;
    console.log(`value: ${text}, type: ${typeof text}`)
    // 출력 값 1, 타입 number
    
    text = '7' + 5;
    console.log(`value: ${text}, type: ${typeof text}`)
    // number 5가 string 5로 바뀌면서 출력 값 '75', 타입 string
    
    text = '8' / '2'
    console.log(`value: ${text}, type: ${typeof text}`) 
    // string 8과 string 2가 둘 다 number로 바뀌면서 출력 값 4, 타입 number

</script>
```

- 이것의 문제점

```html
<script>
    let text = 'hello';

    console.log(text.charAt(0)); // hello의 타입이 string이라 0번째 인덱스 h 출력

    console.log(`value: ${text}, type: ${typeof text}`)
    text = 1;
    console.log(`value: ${text}, type: ${typeof text}`)
    text = '7' + 5;
    console.log(`value: ${text}, type: ${typeof text}`)
    text = '8' / '2'
    console.log(`value: ${text}, type: ${typeof text}`)

    console.log(text.charAt(0)); 위에서 하나씩 처리하며 내려오면서 type이 number로 바뀌어서 0번째 인덱스 못찾고 에러 발생

</script>
```

