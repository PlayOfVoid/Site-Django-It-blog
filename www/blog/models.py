from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

from django.db import models

class PostCategory(models.Model):
    title = models.CharField(max_length=56)
    dsc = models.TextField(max_length=215)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=65)
    dsc = models.TextField(max_length=315)
    text = models.TextField(max_length=4500)
    category = models.ForeignKey(to=PostCategory, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    

class Comment(models.Model):
    author = models.CharField(max_length=35)
    text = models.TextField(max_length=750)


    def __str__(self):
        return f"{self.author}"
    


class PostComment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(to=Comment, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment on {self.post.title} by {self.comment.author}"



    


