from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class PostCategory(models.Model):
    title = models.CharField(max_length=56)
    dsc = models.TextField(max_length=215)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=65)
    dsc = models.TextField(max_length=315)
    text = models.TextField(max_length=4500)
    category = models.ForeignKey(to=PostCategory,on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    


