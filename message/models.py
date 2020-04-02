from django.db import models

# Create your models here.
class Message(models.Model):
    your_name = models.CharField(max_length=30,blank=False,null=False)
    email_address = models.EmailField()
    subject = models.CharField(max_length=20,blank=False,null=False)
    content = models.TextField(max_length=2000,blank=False,null=False)
    def __str__(self):
        return self.your_name