from django.shortcuts import render,HttpResponseRedirect,redirect
from django.urls import reverse
from django.views import View
from .forms import UserLoginForm,UserRegForm,UserProfileForm
from django.contrib import auth
from blog.models import Post,PostCategory
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from blog.models import  Tag
# Create your views here.

class Reg(View):
    def post(self,request):
        form = UserRegForm(data=request.POST)
        if form.is_valid():
            user = form.save() 
            user.save() 
            return redirect('auth:login')
            
        context = {
            'form':form
        }
        return render(request,'auth/reg.html',context)
    

    def get(self, request):
            form = UserRegForm()  # Отображаем пустую форму при GET запросе
            context = {'form': form}
            return render(request, 'auth/reg.html', context)
    

class Login(View):
    def get(self, request):
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'auth/login.html', context)

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(request, username=username, password=password) # Аутентификация пользователя

            if user is not None:
                auth.login(request, user) # Вход пользователя в систему
                return redirect('blog:index') # Перенаправление на главную страницу
            else:
                
                form.add_error(None, "Неверное имя пользователя или пароль.")  

        context = {
            'form': form
        }
        return render(request, 'auth/login.html', context)
    
def logout_view(request):
    auth.logout(request)
    return redirect('blog:index')


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user 
            post.save()
            return redirect('blog:index')
        else:
            print(form.errors)
    else:
        form = ArticleForm()

    posts = Post.objects.all().order_by('-id') #Переименовано articles -> posts
    categories = PostCategory.objects.all() #Переименовано Category -> PostCategory
    tags = Tag.objects.all()
    context = {
        'form': form,
        'articles': posts, # articles -> posts
        'categories': categories,
        'tags':tags,
    }
    return render(request, 'auth/profile.html', context)


    
