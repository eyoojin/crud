from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    
    return render(request, 'index.html', context)

def detail(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post
    }

    return render(request, 'detail.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    post = Post()
    post.title = title
    # models의 title = create의 title
    post.content = content
    post.save()
    # models.Model에게 상속받은 함수

    # return redirect('/index/') # 전체 게시판으로 이동
    return redirect(f'/posts/{post.id}/') # 게시물로 이동