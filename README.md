# CRUD

## 0. setting

- 가상환경 생성/ 활성화
    - `python -m venv venv`
    - `source venv/Scripts/activate`
- `.gitignore` 
    - python, window, macOS, Django

## 1. Django

- 장고 설치
    - `pip install django`
- 프로젝트 생성
```shell
django-admin startproject crud .
```
- 앱 생성
```shell
django-admin startapp posts
```
- 앱 등록 
    - settings.py -> INSTALLED_APPS
- 경로 설정
    - urls.py
```
from posts import views
path('index/', views.index)
```
- views.py에서 index 함수 생성 
- posts/templates/ 폴더 생성
- index.html 파일 생성

## 2. CRUD

- modeling (`models.py`)
```python
class Post(models.Model): #상속
    title = models.CharField(max_length=100)
    content = models.TextField()
```

- migration
    - posts/migrations/0001_initial.py 생성
```shell
# 번역본 생성
python manage.py makemigrations
```
```shell
# DB에 반영
python manage.py migrate
```

- create super user
```shell
python manage.py createsuperuser
```

- admin 페이지에 모델 등록 (`admin.py`)
```python
from .models import Post
# 현재 폴더의 models
admin.site.register(Post)
```

- Read 전체 게시판 기능 만들기 
    - index()

- Read 게시물 기능 만들기
    - detail(id)

- 전체 게시판 <-> 게시물 이동
    - a 태그

- Create 게시물 생성 기능 만들기
    - new()
        1. 사용자에게 빈 종이 제공
        2. 빈 종이에 내용을 입력
        3. 입력된 내용을 create로 전송
    - create()
        4. 전송된 데이터 중에서 필요한 정보를 추출
        5. DB에 저장
        6. 사용자에게 저장된 것을 보여줌 (2가지 중 선택)
            - index로 이동
            - detail로 이동
```python
from django.shortcuts import redirect
```

- Delete 게시물 삭제 기능 만들기
    - delete()
        1. 사용자가 삭제 버튼을 누름
        2. 몇 번 게시물을 삭제할지 **탐색**
        3. 해당 게시물을 **삭제**

- Update 게시물 수정 기능 만들기
    - edit()
        1. 기존 정보 보여주기(R)
    - update()
        2. 수정된 정보로 덮어쓰기(C)
            3. 기존 정보 가져오기
            4. 새로운 정보 가져오기
            5. 기존 정보를 새로운 정보로 바꾸기

---
### Crud

- 데이터로 할 수 있는 4가지
    - Create: 생성
    - Read: 읽기
    - Update: 갱신
    - Delete: 삭제
    
- DB
    - settings.py -> DATABASES -> 'ENGINE': 'django.db.backends.sqlite3' -> `db.sqlite3`

- ORM: 번역기
    - Object(Python 세상) | Relational(DB, SQL 세상) Mapping