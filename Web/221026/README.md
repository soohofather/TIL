## 2022년 10월 26일(수)

> 과정 외 시간 - 동기? 비동기? - Ajax, axios



```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
  <button>클릭</button>
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    const body = document.querySelector('body')
    const title = document.createElement('h1')
    title.innerText = 'AJAX'
    body.appendChild(title)

    const button = document.querySelector('button')
    button.addEventListener('click', function () {
      const URL = 'https://jsonplaceholder.typicode.com/todos/1'
      axios.get(URL)
        .then(response => {
          const h2 = document.createElement('h2')
          h2.innerText = response.data.title
          body.appendChild(h2)
          const p = document.createElement('p')
          p.innerText = response.data.userId
          body.appendChild(p)
        })
        .catch(err => console.log(`${err}!!!`))
    })
  </script>
</body>

</html>
```

