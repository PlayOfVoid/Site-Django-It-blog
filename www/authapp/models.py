from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/avatar_image',blank=True,null=True,)

    def __str__(self):
        return f"{self.username}({self.id})" 
    
class Subscribe(models.Model):
    author = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="authors")
    subscriber = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="subscribers")
    mute = models.BooleanField(default=False)
    is_subscribe = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.author} | {self.subscriber}"


    

