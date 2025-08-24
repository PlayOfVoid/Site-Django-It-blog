from django import forms
from .models import User
from blog.models import Post
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password')

class UserRegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2')



class UserProfileForm(UserChangeForm):
    class Meta:
        model = User 
        fields = ('username','password')



class ArticleForm(forms.ModelForm):#форма для создания статьи
    class Meta:
        model = Post
        fields = ['title', 'description', 'content', 'category'] # Добавлено dsc


    