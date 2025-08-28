from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from .models import Post,PostCategory,Comment
from .forms import CommentForm
from authapp.models import Subscribe
from authapp.models import User
from . import myfunc
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
    
    #  Получаем все Comment, связанные с данным постом
  
    #  Преобразуем Comment в список Comment объектов
    comments = list(Comment.objects.filter(post=post))

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            #comment = form.save()  #  Сохраняем Comment
            text = form.cleaned_data['text']
            author = form.cleaned_data['author']
            Comment.objects.create(post=post, text=text, author=author) # Создаем и сохраняем Comment
            return redirect('blog:detail_post', pk=pk) #  Перенаправляем на эту же страницу
    else:
        form = CommentForm() # Создаем пустую форму

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog/post_detail.html', context)




def subscribe(request, author_id):
    author = get_object_or_404(User, pk=author_id)
    subscriber = request.user
    if author == subscriber:
        return HttpResponse('Вы не можете подписаться сами на себя!')

    subscribe, created = Subscribe.objects.get_or_create(
        author=author,
        subscriber=subscriber,
        defaults={'mute': False, 'is_subscribe': False}
    )

    # Переключение статуса подписки
    subscribe.is_subscribe = not subscribe.is_subscribe
    subscribe.save()
    
   

    return redirect(request.META.get('HTTP_REFERER', '/'))


