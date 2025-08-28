from django.urls import path
from . import views 
from blog import views as blog

app_name = 'auth'

urlpatterns = [
    path('login/',views.Login.as_view(),name='login'),
    path('register/',views.Reg.as_view(),name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('profile/',views.profile_view,name='profile'),
    path('is_subscribe/<int:author_id>/',blog.subscribe,name='is_sub'),

]