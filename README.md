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
- 앱 생성/ 등록
```shell
django-admin startapp posts
```
- 
```
from posts import views
path('index/', views.index)
```
- posts/templates/