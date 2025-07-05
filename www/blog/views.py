from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,PostCategory,Comment,PostComment
from .forms import CommentForm

# Create your views here.

def index(request):
    return render(request,'blog/index.html')

def posts(request):
    posts = Post.objects.all()

    context = {
        'posts':posts,
    }
    return render(request,'blog/posts.html',context)

def detail_post(request, pk):
    post = get_object_or_404(Post, pk=pk) #  Получаем пост или возвращаем 404
    
    #  Получаем все PostComment, связанные с данным постом
    post_comments = PostComment.objects.filter(post=post)
    #  Преобразуем PostComment в список Comment объектов
    comments = [pc.comment for pc in post_comments]

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()  #  Сохраняем Comment
            post_comment = PostComment.objects.create(post=post, comment=comment) # Создаем и сохраняем PostComment
            return redirect('blog:detail_post', pk=pk) #  Перенаправляем на эту же страницу
    else:
        form = CommentForm() # Создаем пустую форму

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog/post_detail.html', context)
