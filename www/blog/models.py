from django.db import models
from django.contrib.auth.models import AbstractUser
from authapp.models import User
# Create your models here.

from django.db import models

class PostCategory(models.Model):
    title = models.CharField(max_length=56)
    description = models.TextField(max_length=215,blank=True,null=True)

    def __str__(self):
        return self.title
    
    
class Tag(models.Model):
    title = models.CharField(max_length=25,blank=True,null=True)
    description = models.TextField(max_length=215,blank=True,null=True)
    
    def __str__(self):
        return self.title



class Post(models.Model):
    slug = models.SlugField(max_length=300,unique=True)
    title = models.CharField(max_length=256,unique=True,)
    description = models.TextField(max_length=315)
    content = models.TextField(max_length=4500)
    category = models.ForeignKey(to=PostCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField(to=Tag,related_name='posts')
    author = models.ForeignKey(to=User,on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog/blog_images',blank=True,null=True)
    
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title}({self.id})"
    

class Comment(models.Model):
    author = models.ForeignKey(to=User,on_delete=models.CASCADE)
    text = models.TextField(max_length=750)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE) 
    create_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Comment on {self.post.title} by {self.author}"
    





    


