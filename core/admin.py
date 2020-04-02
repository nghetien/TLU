from django.contrib import admin
from message.models import Message
from news.models import Post
# Register your models here.

admin.site.register(Message)
admin.site.register(Post)