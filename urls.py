from django.contrib import admin
from django.urls import path, include
from blog_app.views import index, page1, page2, page, article_show_all


urlpatterns = [
    path('', index),
    path('index/', index),
    path('page1/', page1, name='page1'),
    path('page2/', page2, name='page2'),
    path('page/<int:num_page>', page, name='page'),
    path('article_all/', article_show_all, name='article_show_all'),

]


