from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Subscribe(models.Model):
    author = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="authors")
    subscriber = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="subscribers")
    mute = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.author} | {self.subscriber}"

