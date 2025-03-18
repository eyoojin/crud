"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Read (All)
    path('posts/', views.index), # 수정
    # Read (1)
    path('posts/<int:id>/', views.detail),
    # Create
    path('posts/new/', views.new),
    path('posts/create/', views.create),
    # Delete
    path('posts/<int:id>/delete/', views.delete),
    # 하나의 링크로 두개의 동작을 할 수 없기 때문에 새로운 링크 생성
    # Update
    path('posts/<int:id>/edit/', views.edit),
    path('posts/<int:id>/update/', views.update)
]
