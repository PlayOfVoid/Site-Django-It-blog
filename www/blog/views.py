from django.shortcuts import render,get_object_or_404
from .models import Post,PostCategory

# Create your views here.

def index(request):
    return render(request,'blog/index.html')

def posts(request):
    posts = Post.objects.all()

    context = {
        'posts':posts,
    }
    return render(request,'blog/posts.html',context)

def detail_post(request,pk):
    context = {
        'post':get_object_or_404(Post,pk=pk)
    }
    return render(request,'blog/post_detail.html',context)
