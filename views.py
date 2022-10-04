from django.shortcuts import render
from django.http import HttpResponse
from blog_app.models import Article, Category

# Create your views here.

def article_show_all(request):
    data = Article.objects.all()
    return render(request, 'blog_app/article_show_all.html', {data: data})


def index(request):
    return HttpResponse('<h1>Hello world!!!</h1>')


def page1(request):
    return render(request, 'blog_app/page1.html')

def page2(request):
    return render(request, 'blog_app/page2.html')

def page(request, page_num):
    if page_num == 1:
        return render(request, 'blog_app/page1.html')
    elif page_num == 2:
        return render(request, 'blog_app/page2.html')