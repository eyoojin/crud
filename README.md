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
```shell
# 번역본 생성
python manage.py makemigrations
```
    - posts/migrations/0001_initial.py
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