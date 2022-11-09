# 2022년 10월 18일 (화)

> Django13! 댓글 작성 (1 : N, one to many relationship)



`수호아빠의 한마디: 컨디션 조금 회복.. 잃어버린 Django ORM 기억 회복중  `



### 1. 댓글 작성 및 삭제 (1 : N, one to many relationship)

- 게시글은 댓글을 0개 이상 가진다.
  - 1개의 게시글은 여러 개의 댓글을 가진다.
  - 1개의 게시글은 0개의 댓글을 가질수도 있다.
- 1개의 댓글은 반드시 1개의 게시글에 속한다.

![Django1018](assets/Django1018.gif)

- `models.py`
  - on_delete 옵션 값 (외래 키가 참조하는 객체가 사라졌을 때,  외래 키를 가진 객체를 어떻게 처리할 지를 정의)
    - CASCADE : 부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제
    - PROTECT, SET_NULL, SET_DEFAULT … 등 여러 옵션 값들이 존재

```python
class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
```

- `urls.py`

```python
urlpatterns = [
    ...
    path("comment/<int:pk>", views.c_create, name="c_create"),
    ...
]
```

- `views.py`에서 댓글 생성
  - Comment 테이블에 content만 넣고 저장을하면 에러뜸
    - 1개의 Comment는 1개의 article을 가져야하기때문에 (1:N)
  - Comment의 content를 넣은 후 `commit=False`를 사용하여 저장을 멈춤
  - 그리고 `comment.article`에 article.objects.get(pk=pk)를 넣어주고
  - 저장

```python
def c_create(request, pk):

    comment_form = CommentForm(request.POST)
    article = Article.objects.get(pk=pk)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()

    return redirect("article:detail", pk)
```

- `views.py`에서 댓글 불러오기
  - 역참조 개념
    - 1:N에서는 1이 N을 참조하는 상황
    - 아래 댓글을 불러오는 것은 N에서 1을 역참조 하는 상황
  - Article 클래스에서 Comment와 아무런 관계가 작성되어있지 않음
    - article.comment 형식으로는 댓글 객체를 참조 할 수 없음
  - 반면 반대로는 ForeignKey 클래스로 article이 있음
    - comment.article 형태로 작성 가능
  - article.comment_set.method()
    - 이러한 이유로 comment에서 article을 역참조 할 때는 article.comment_set을 이용.

```python
def detail(request, pk):

    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comment = article.comment_set.all()

    context = {
        "article": article,
        "comment_form": comment_form,
        "comment": comment,
    }

    return render(request, "article/detail.html", context)
```

