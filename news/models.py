from django.db import models

# Create your models here.

class Post(models.Model):
    type = models.CharField(max_length=20,null=True)
    user_post = models.CharField(max_length=30,default='',null=True)
    title = models.CharField(max_length=255,default='')
    content1 = models.TextField(null=True)
    content2 = models.TextField(null=True)
    note = models.CharField(max_length=500,default='',null=True)
    image_title = models.ImageField(null=True)
    image_1 = models.ImageField(null=True)
    image_2 = models.ImageField(null=True)
    views = models.IntegerField(default=0,null=True)
    date_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title