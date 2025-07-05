from django.urls import path
from . import views as blog

app_name = 'blog'


urlpatterns = [
    path('',blog.index,name='index'),
    path('posts/',blog.posts,name='posts'),
    path('detail_post/<int:pk>/',blog.detail_post,name='detail_post'),
]  