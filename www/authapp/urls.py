from django.urls import path
from . import views as auth

app_name = 'auth'

urlpatterns = [
    path('login/',auth.Login.as_view(),name='login'),
    path('register/',auth.Reg.as_view(),name='register'),
    path('logout/',auth.logout_view,name='logout'),
    path('profile/',auth.profile_view,name='profile')
]