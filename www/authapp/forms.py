from django import forms
from django.contrib.auth.models import User
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


    